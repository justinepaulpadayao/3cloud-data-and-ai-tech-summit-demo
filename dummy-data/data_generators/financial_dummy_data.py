import sys
import json
import random
import uuid
import gzip
import re
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from typing import Dict, List, Any, Generator
from pathlib import Path

class FinancialDataGenerator:
    def __init__(self, config_path: str = "data_gen_config.json"):
        self.faker = Faker()
        self.config = self._load_config(config_path)
        self.metadata = {
            "generated_issues": {},
            "schema_versions": [],
            "data_stats": {}
        }
        
        # Initialize issue counters
        for issue_type in ['nulls', 'duplicates', 'outliers', 'invalids', 'corruptions']:
            self.metadata['generated_issues'][issue_type] = 0

    def _load_config(self, config_path: str) -> Dict:
        """Load JSON configuration with default fallback"""
        default_config = {
            "base_records": 1000,
            "duplicate_rate": 0.02,
            "null_rate": 0.05,
            "outlier_rate": 0.01,
            "corruption_rate": 0.005,
            "schema_variation_rate": 0.1,
            "date_formats": ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"],
            "currency_codes": ["USD", "EUR", "GBP", "JPY", "CAD"],
            "countries": ["US", "UK", "CA", "DE", "FR"],
            "output_format": "parquet",
            "chunk_size": 10000
        }
        
        try:
            with open(config_path) as f:
                user_config = json.load(f)
                return {**default_config, **user_config}
        except FileNotFoundError:
            return default_config

    def _apply_data_quality_issues(self, record: Dict, entity: str) -> Dict:
        """Apply configured data quality issues"""
        # Null injection
        if random.random() < self.config['null_rate']:
            null_field = random.choice(list(record.keys()))
            record[null_field] = None
            self.metadata['generated_issues']['nulls'] += 1

        # Format inconsistencies
        if 'date' in record and random.random() < 0.1:
            record['date'] = self.faker.date_time().strftime(
                random.choice(self.config['date_formats'])
            )

        # Data type corruption
        if random.random() < self.config['corruption_rate']:
            target_field = random.choice(list(record.keys()))
            if isinstance(record[target_field], (int, float)):
                # Controlled numeric corruption that preserves type safety
                corruption_type = random.choice([
                    lambda x: float('nan'),  # Valid NaN
                    lambda x: x * 1000,      # Scaling issue
                    lambda x: x + random.uniform(-x*0.5, x*0.5),  # Precision error
                    lambda x: float('inf')   # Valid infinity
                ])
                record[target_field] = corruption_type(record[target_field])
            elif isinstance(record[target_field], str):
                record[target_field] = self._inject_special_chars(record[target_field])
        
        return record

    def _inject_special_chars(self, value: str) -> str:
        """Inject special characters into string values"""
        corruption_patterns = [
            lambda s: s + random.choice(['', '§', '€', '¥']),
            lambda s: s.encode('latin-1').decode('utf-8', 'ignore'),
            lambda s: re.sub(r'\d', lambda m: str(random.randint(0,9)), s)
        ]
        return random.choice(corruption_patterns)(value)

    def generate_customer(self, customer_id: str) -> Dict:
        """Generate customer record with embedded issues"""
        country = random.choice(self.config['countries'])
        customer = {
            "customer_id": customer_id,
            "name": self.faker.name(),
            "address": self.faker.address(),
            "tax_id": self.faker.ssn(),
            "incorporation_date": self.faker.date_between('-10y', '-1y').isoformat(),
            "country_code": country,
            "business_type": random.choice(["LLC", "Corp", "Partnership"]),
            "risk_category": random.choice(["Low", "Medium", "High"])
        }
        return self._apply_data_quality_issues(customer, 'customer')

    def generate_account(self, account_id: str, customer_id: str) -> Dict:
        """Generate account record with balance logic"""
        currency = random.choice(self.config['currency_codes'])
        account = {
            "account_id": account_id,
            "customer_id": customer_id,
            "opening_date": self.faker.date_time_this_decade().isoformat(),
            "base_currency": currency,
            "current_balance": round(random.uniform(1000, 1000000), 2),
            "credit_limit": round(random.uniform(10000, 500000), 2),
            "status": random.choice(["Active", "Dormant", "Closed"])
        }
        return self._apply_data_quality_issues(account, 'account')

    def generate_transaction(self, transaction_id: str, account_id: str) -> Dict:
        """Generate transaction with temporal consistency"""
        transaction = {
            "transaction_id": transaction_id,
            "account_id": account_id,
            "timestamp": self.faker.date_time_this_year().isoformat(),
            "amount": round(random.uniform(-50000, 200000), 2),
            "currency": random.choice(self.config['currency_codes']),
            "counterparty": self.faker.company(),
            "transaction_type": random.choice(["Wire", "ACH", "Card", "FX"]),
            "description": self.faker.text(max_nb_chars=50)
        }
        
        # Add FX conversion artifacts
        if random.random() < 0.3 and transaction['currency'] != 'USD':
            transaction['converted_amount'] = round(
                transaction['amount'] * random.uniform(0.8, 1.2), 2
            )
            transaction['exchange_rate'] = round(random.uniform(0.8, 1.2), 4)
        
        return self._apply_data_quality_issues(transaction, 'transaction')

    def generate_chunk(self, entity: str, chunk_size: int) -> Generator[Dict, None, None]:
        """Generate data in memory-efficient chunks"""
        for _ in range(chunk_size):
            entity_id = str(uuid.uuid4())
            if entity == "customer":
                yield self.generate_customer(entity_id)
            elif entity == "account":
                yield self.generate_account(entity_id, str(uuid.uuid4()))
            elif entity == "transaction":
                yield self.generate_transaction(entity_id, str(uuid.uuid4()))

    def write_data(self, entity: str, output_dir: str):
        """Write generated data with format-specific handling"""
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        chunk_size = self.config['chunk_size']
        total_records = self.config['base_records']
        
        writers = {
            'csv': lambda df, path: df.to_csv(path, index=False),
            'json': lambda df, path: df.to_json(path, orient='records'),
            'parquet': lambda df, path: pq.write_table(pa.Table.from_pandas(df), path)
        }
        
        for chunk_num, i in enumerate(range(0, total_records, chunk_size)):
            chunk = self.generate_chunk(entity, min(chunk_size, total_records - i))
            df = pd.DataFrame(chunk)
            
            # Apply schema variations
            if random.random() < self.config['schema_variation_rate']:
                df = self._apply_schema_variation(df)
            
            output_path = f"{output_dir}/{entity}_part_{chunk_num}.{self.config['output_format']}"
            writers[self.config['output_format']](df, output_path)
            
            # Add compression for large files
            if self.config['output_format'] == 'csv' and total_records > 100000:
                with open(output_path, 'rb') as f_in:
                    with gzip.open(f"{output_path}.gz", 'wb') as f_out:
                        f_out.writelines(f_in)
                Path(output_path).unlink()

    def _apply_schema_variation(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply schema variations to dataframe"""
        variation_type = random.choice([
            'column_order', 'extra_fields', 'missing_fields', 'type_change'
        ])
        
        if variation_type == 'column_order':
            cols = df.columns.tolist()
            random.shuffle(cols)
            return df[cols]
        
        elif variation_type == 'extra_fields':
            new_col = f"extra_{self.faker.word()}"
            return df.assign(**{new_col: np.nan})
        
        elif variation_type == 'missing_fields':
            if len(df.columns) > 1:
                return df.drop(columns=random.choice(df.columns))
            return df
        
        elif variation_type == 'type_change':
            col = random.choice(df.columns)
            df[col] = df[col].astype(str)
            return df

    def save_metadata(self, output_dir: str):
        """Save generation metadata and validation schema"""
        meta_path = Path(output_dir) / "generation_metadata.json"
        with open(meta_path, 'w') as f:
            json.dump(self.metadata, f, indent=2)
        
        # Generate validation schema
        validation_schema = {
            "expected_schema": {
                "customer": list(self.generate_customer("sample").keys()),
                "account": list(self.generate_account("sample", "sample").keys()),
                "transaction": list(self.generate_transaction("sample", "sample").keys())
            },
            "data_quality_rules": {
                "null_thresholds": self.config['null_rate'],
                "duplicate_rate": self.config['duplicate_rate'],
                "currency_codes": self.config['currency_codes']
            }
        }
        
        schema_path = Path(output_dir) / "validation_schema.json"
        with open(schema_path, 'w') as f:
            json.dump(validation_schema, f, indent=2)

if __name__ == "__main__":
    generator = FinancialDataGenerator()
    
    # Generate all entity types
    for entity in ["customer", "account", "transaction"]:
        generator.write_data(entity, f"generated_data/{entity}")
    
    # Save metadata and validation schema
    generator.save_metadata("generated_data/")