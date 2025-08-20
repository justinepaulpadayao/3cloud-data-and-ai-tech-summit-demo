import json
import pandas as pd
import numpy as np
import pyarrow.parquet as pq
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
import re

@dataclass
class DataQualityReport:
    null_counts: Dict[str, int]
    type_mismatches: Dict[str, Tuple[str, str]]
    schema_violations: Dict[str, List[str]]
    duplicate_count: int
    anomaly_stats: Dict[str, Dict[str, float]]
    corruption_patterns: Dict[str, Dict[str, int]]
    currency_violations: Dict[str, List[str]]
    date_format_issues: int

class FinancialDataValidator:
    def __init__(self, data_path: str, schema_path: str):
        self.data_path = data_path
        self.schema = self._load_schema(schema_path)
        self.report = DataQualityReport(
            null_counts={},
            type_mismatches={},
            schema_violations={},
            duplicate_count=0,
            anomaly_stats={},
            corruption_patterns={},
            currency_violations={},
            date_format_issues=0
        )
        
    def _load_schema(self, schema_path: str) -> Dict:
        with open(schema_path) as f:
            return json.load(f)
    
    def _load_file(self, file_path: Path) -> pd.DataFrame:
        if file_path.suffix == '.parquet':
            return pq.read_table(file_path).to_pandas()
        elif file_path.suffix == '.json':
            return pd.read_json(file_path)
        return pd.read_csv(file_path)

    def _detect_nulls(self, df: pd.DataFrame):
        null_counts = df.isnull().sum().to_dict()
        for col, count in null_counts.items():
            self.report.null_counts[col] = self.report.null_counts.get(col, 0) + count

    def _detect_type_mismatches(self, df: pd.DataFrame, entity: str):
        expected_types = self.schema['expected_schema'][entity]
        for col in expected_types:
            if col not in df.columns:
                continue
                
            expected_type = type(df[col].dropna().iloc[0]) if not df[col].empty else str
            actual_type = df[col].dtype
            
            if not pd.api.types.is_dtype_equal(actual_type, np.dtype(expected_type)):
                self.report.type_mismatches[col] = (
                    str(expected_type), 
                    str(actual_type)
                )

    def _detect_schema_violations(self, df: pd.DataFrame, entity: str):
        expected_cols = set(self.schema['expected_schema'][entity])
        actual_cols = set(df.columns)
        
        missing = expected_cols - actual_cols
        extra = actual_cols - expected_cols
        
        if missing:
            self.report.schema_violations.setdefault(entity, []).extend(
                f"Missing columns: {', '.join(missing)}"
            )
        if extra:
            self.report.schema_violations.setdefault(entity, []).extend(
                f"Extra columns: {', '.join(extra)}"
            )

    def _detect_duplicates(self, df: pd.DataFrame, entity: str):
        pk_column = f"{entity}_id"
        if pk_column in df.columns:
            duplicates = df.duplicated(subset=[pk_column]).sum()
            self.report.duplicate_count += duplicates

    def _detect_anomalies(self, df: pd.DataFrame):
        for col in df.select_dtypes(include=np.number):
            if df[col].nunique() < 2:
                continue
                
            z_scores = (df[col] - df[col].mean()) / df[col].std()
            outliers = np.abs(z_scores) > 3
            self.report.anomaly_stats[col] = {
                'mean': df[col].mean(),
                'std': df[col].std(),
                'outlier_count': outliers.sum(),
                'min': df[col].min(),
                'max': df[col].max()
            }

    def _detect_corruption(self, df: pd.DataFrame):
        corruption_patterns = {
            'special_chars': re.compile(r'[^\w\s-]'),
            'encoding_errors': re.compile(r'[\x80-\xFF]'),
            'invalid_numbers': re.compile(r'[^0-9\.-]')
        }
        
        for col in df.select_dtypes(include='object'):
            counts = {pattern: 0 for pattern in corruption_patterns}
            for value in df[col].dropna().astype(str):
                for pattern_name, pattern in corruption_patterns.items():
                    if pattern.search(value):
                        counts[pattern_name] += 1
            
            if any(counts.values()):
                self.report.corruption_patterns[col] = counts

    def _validate_currency(self, df: pd.DataFrame):
        if 'currency' in df.columns:
            valid_currencies = self.schema['data_quality_rules']['currency_codes']
            invalid = df[~df['currency'].isin(valid_currencies)]
            if not invalid.empty:
                self.report.currency_violations['currency'] = invalid['currency'].unique().tolist()

    def _validate_dates(self, df: pd.DataFrame):
        date_cols = [col for col in df.columns if 'date' in col.lower()]
        valid_formats = [
            r'\d{4}-\d{2}-\d{2}', 
            r'\d{2}/\d{2}/\d{4}', 
            r'\d{2}-\d{2}-\d{4}'
        ]
        
        for col in date_cols:
            if df[col].dtype == 'object':
                format_matches = df[col].astype(str).str.match(
                    f'^({"|".join(valid_formats)})$'
                )
                self.report.date_format_issues += (~format_matches).sum()

    def validate_entity(self, entity: str):
        """Main validation workflow"""
        for file_path in Path(self.data_path).glob(f"{entity}_part_*"):
            df = self._load_file(file_path)
            
            self._detect_schema_violations(df, entity)
            self._detect_nulls(df)
            self._detect_type_mismatches(df, entity)
            self._detect_duplicates(df, entity)
            self._detect_anomalies(df)
            self._detect_corruption(df)
            self._validate_currency(df)
            self._validate_dates(df)

    def generate_report(self, output_path: str):
        """Save validation report as JSON"""
        report_data = {
            'null_counts': self.report.null_counts,
            'type_mismatches': self.report.type_mismatches,
            'schema_violations': self.report.schema_violations,
            'duplicate_count': self.report.duplicate_count,
            'anomaly_stats': self.report.anomaly_stats,
            'corruption_patterns': self.report.corruption_patterns,
            'currency_violations': self.report.currency_violations,
            'date_format_issues': self.report.date_format_issues
        }
        
        with open(Path(output_path) / "data_quality_report.json", 'w') as f:
            json.dump(report_data, f, indent=2)

if __name__ == "__main__":
    validator = FinancialDataValidator(
        data_path="generated_data",
        schema_path="generated_data/validation_schema.json"
    )
    
    for entity in ["customer", "account", "transaction"]:
        validator.validate_entity(entity)
    
    validator.generate_report("validation_reports/")