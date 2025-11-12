# PySpark & Python Coding Standards - AI Memory Bank

## Core Principles
- Code readability over cleverness
- Consistency within project > consistency with style guide
- Create testable, maintainable code
- Never break backwards compatibility for style compliance

## Code Layout

### Line Length
- **Maximum**: 79 characters for code
- **Comments/Docstrings**: 72 characters

### Indentation
- **Use spaces only** (no tabs)
- **4 spaces** per indentation level
- Continuation lines: align vertically or use hanging indent
- Add extra indentation for multi-line conditionals to distinguish from nested code

### Line Breaks
- Break **before** binary operators (mathematical convention)
- Use parentheses for multi-line expressions (avoid `\` continuation)

### Blank Lines
- **2 blank lines** around top-level functions and classes
- **1 blank line** around methods inside classes
- Use blank lines to separate logical sections within functions

## Import Standards

### Structure
```python
# Standard library imports
import os
import sys

# Third-party imports
import pandas as pd
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql import Window as W

# Local application imports
from myapp.utils import helper_function
```

### Rules
- One import per line (except from same package)
- Group imports: stdlib → third-party → local (blank line between groups)
- Use absolute imports
- **Never use wildcard imports** (`from module import *`)

### PySpark Specific
```python
from pyspark.sql import functions as F  # Always use F
from pyspark.sql import types as T      # Always use T
from pyspark.sql import Window as W     # Always use W
```

## Naming Conventions

### Standard Styles
| Type | Convention | Example |
|------|------------|---------|
| Variable | lower_snake_case | `x`, `a_variable_name` |
| Constant | UPPER_SNAKE_CASE | `DEFAULT_SIZE` |
| Function | lower_snake_case | `approx_equal`, `hash_code` |
| Class | PascalCase | `Customer`, `VendorProduct` |
| Module/Package | lowercase | `commonfunctions` |
| DataFrame Columns | PascalCase | `FirstName`, `HireDate` |

### Variable Naming
- **Collections**: Use plural names (e.g., `users`, not `user_list`)
- **DataFrames**: Suffix with `_df` (e.g., `customers_df`)
- Never use `l`, `O`, `I` as single-character names (confusion with 1, 0)

### Function Arguments (PySpark)
```python
def transform(df):  # Generic dataframe argument
def with_column(col): # Single column argument
def compare(col1, col2):  # Two columns
def select_columns(*cols):  # Multiple columns
def rename(col_name):  # String column name
```

Use suffixes for specificity: `key_cols`, `source_df`, `target_df`

### Function Name Prefixes (PySpark)
- **`with_`**: Adds columns
  - `with_cool_cat()` → adds `CoolCat` column
  - `with_is_nice_person()` → adds `IsNicePerson` column
- **`filter_`**: Removes rows
  - `filter_negative_growth_rate()` → removes negative growth
  - `filter_invalid_zip_codes()` → removes bad zip codes
- **`enrich_`**: Clobbers existing columns (avoid when possible)
- **`explode_`**: Expands rows into multiple rows

### Standard Abbreviations
- `gt`: greater than
- `lt`: less than
- `leq`: less than or equal
- `geq`: greater than or equal
- `eq`: equal to
- `between`: between two values

## String Conventions

### Quotes
- **Default**: Use double quotes `"string"`
- **Exception**: Use single quotes when string contains double quotes
- **Triple-quoted strings**: Always use double quotes `"""docstring"""`

### String Interpolation
**Prefer f-strings** (Python 3.6+):
```python
# Good
message = f"Hello {name}, you are {age} years old"

# Avoid
message = "Hello {}, you are {} years old".format(name, age)
message = "Hello " + name + ", you are " + str(age) + " years old"
```

## Whitespace Rules

### Avoid Extra Whitespace
- Inside parentheses/brackets/braces: `spam(ham[1], {eggs: 2})`
- Before comma/semicolon/colon: `if x == 4: print(x, y); x, y = y, x`
- Before function call parentheses: `spam(1)`
- Before indexing/slicing brackets: `dct['key']`
- Around assignment for alignment

### Binary Operators
- Always single space on both sides: `x = 1`, `x == 2`, `x >= 3`
- For mixed priorities, consider spacing around lower priority operators

## Comparison Best Practices

### Boolean Comparisons
```python
# Good
if greeting:
    pass

# Bad
if greeting == True:
    pass
```

### Sequence Checks
```python
# Good
if not seq:
    pass
if seq:
    pass

# Bad
if len(seq) == 0:
    pass
if len(seq):
    pass
```

### None Comparisons
```python
# Good
if x is not None:
    pass

# Bad
if not x is None:
    pass
if x != None:
    pass
```

### String Prefix/Suffix
```python
# Good
if filename.endswith('.txt'):
    pass
if line.startswith('prefix'):
    pass

# Bad
if filename[-4:] == '.txt':
    pass
if line[:6] == 'prefix':
    pass
```

## Function Best Practices

### Lambda vs Def
```python
# Good
def f(x):
    return 2 * x

# Bad
f = lambda x: 2 * x
```
**Reason**: Named functions provide better tracebacks and representations

### Return Statements
**Be consistent**: Either all returns have expressions or all explicitly return None
```python
# Good
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

# Bad
def foo(x):
    if x >= 0:
        return math.sqrt(x)
```

## PySpark Specific Standards

### Column Functions
Extract complex logic into reusable column functions:
```python
def is_adult(col):
    """Check if age indicates adult."""
    return F.col(col) >= 18

def full_name(first_col, last_col):
    """Concatenate first and last name."""
    return F.concat(F.col(first_col), F.lit(" "), F.col(last_col))
```

### Transform Functions
Structure code as dataframe transformations:
```python
def with_adult_flag(df):
    """Add IsAdult column based on Age."""
    return df.withColumn("IsAdult", F.col("Age") >= 18)

def filter_active_users(df):
    """Keep only active users."""
    return df.filter(F.col("Status") == "active")
```

### Avoid UDFs
**Minimize UDF usage** - use native PySpark functions whenever possible

### Select vs withColumn
- **Single column operation**: Use `.withColumn()`
- **Multiple column operations**: Use `.select()`
- Use select at beginning/end of transforms to define schema contract

### Column Selection Preference Order
```python
# 1. String name (preferred)
df.select("FirstName", "LastName")

# 2. Column object
df.select(F.col("FirstName"), F.col("LastName"))

# 3. Direct access
df.select(df.FirstName, df.LastName)

# 4. Bracket notation (least preferred)
df.select(df["FirstName"], df["LastName"])
```

### Avoid Iteration - Use List Comprehension
```python
# Good
cols_to_keep = ["FirstName", "LastName", "Age"]
df.select([F.col(c) for c in cols_to_keep])

# Bad
for col in cols_to_keep:
    df = df.select(F.col(col))
```

### Column Renaming and Casting
```python
# Good - use aliases
df.select(
    F.col("FirstName").alias("first_name"),
    F.col("Age").cast("integer").alias("age_int")
)

# Bad - use withColumnRenamed
df.withColumnRenamed("FirstName", "first_name")
```

### Refactor Complex Logic
Extract complex conditions into named variables:
```python
# Good
is_late = F.datediff(F.col("DeliveryDate"), F.col("DueDate")) > 0
is_overdue = F.datediff(F.current_date(), F.col("DueDate")) > 30
needs_attention = is_late | is_overdue

df.filter(needs_attention)

# Bad
df.filter(
    (F.datediff(F.col("DeliveryDate"), F.col("DueDate")) > 0) |
    (F.datediff(F.current_date(), F.col("DueDate")) > 30)
)
```

### Sorting
```python
# Good - use SQL functions
df.orderBy(F.asc("Age"), F.desc("Name"))

# Bad - use column methods
df.orderBy(df.Age.asc(), df.Name.desc())
```

### SQL Statements
```python
# Good - assign to variable first
query = """
    SELECT FirstName, LastName, Age
    FROM users
    WHERE Age >= 18
"""
result_df = spark.sql(query)

# Bad - inline SQL
result_df = spark.sql("SELECT FirstName, LastName, Age FROM users WHERE Age >= 18")
```

## Exception Handling

### Exception Chaining
```python
# Good - preserve traceback
try:
    process_data()
except KeyError as e:
    raise ValueError("Invalid data format") from e

# Deliberate replacement - transfer details
try:
    value = obj[key]
except KeyError:
    raise AttributeError(f"Attribute {key} not found") from None
```

## Code Review Checklist

### Readability
- [ ] Line length ≤ 79 characters
- [ ] Proper indentation (4 spaces)
- [ ] Descriptive variable names
- [ ] Complex logic extracted to functions
- [ ] Comments only where necessary

### PySpark Specific
- [ ] DataFrames suffixed with `_df`
- [ ] Imports use F, T, W aliases
- [ ] Column functions used for reusable logic
- [ ] Transform functions for dataframe operations
- [ ] No UDFs (unless absolutely necessary)
- [ ] Select statements define schema contracts
- [ ] List comprehension instead of loops
- [ ] Complex filters extracted to variables

### Testing
- [ ] Functions are unit testable
- [ ] Column functions can be tested independently
- [ ] Transform functions have clear inputs/outputs
- [ ] Edge cases considered

### Performance
- [ ] No redundant operations
- [ ] Efficient column selection
- [ ] Appropriate use of caching (if applicable)
- [ ] No unnecessary UDFs

## Quick Reference

### Must Do
✅ Use spaces (not tabs)
✅ 4 spaces per indent
✅ Double quotes for strings
✅ f-strings for interpolation
✅ Import PySpark as F, T, W
✅ Suffix DataFrames with `_df`
✅ Use transform functions
✅ Extract complex logic
✅ List comprehension over loops

### Must Not Do
❌ Lines > 79 characters
❌ Wildcard imports
❌ Compare booleans with ==
❌ Use l, O, I as variable names
❌ Lambda assignments
❌ Multiple `.withColumn()` calls
❌ Iterate over columns
❌ Use UDFs unnecessarily
❌ Inline complex logic

## Context for AI Assistant

When reviewing or generating code:
1. **Prioritize readability** - code is read more than written
2. **Apply conventions consistently** within the file/module
3. **Extract complexity** - break down complex logic into named components
4. **Test-driven mindset** - write code that's easy to unit test
5. **PySpark optimization** - leverage native functions over UDFs
6. **Schema clarity** - use select statements to define data contracts