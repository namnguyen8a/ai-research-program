
## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Importing pandas](#importing-pandas)
4. [Core Data Structures](#core-data-structures)

   * [Series](#series)
   * [DataFrame](#dataframe)
5. [Creating Series and DataFrames](#creating-series-and-dataframes)

   * [From Python Structures](#from-python-structures)
   * [From NumPy Arrays](#from-numpy-arrays)
   * [From Dictionaries](#from-dictionaries)
   * [From External Files or Databases](#from-external-files-or-databases)
6. [Inspecting Data](#inspecting-data)

   * [Viewing Top/Bottom Rows](#viewing-topbottom-rows)
   * [Information and Summary Statistics](#information-and-summary-statistics)
   * [DataFrame Attributes](#dataframe-attributes)
7. [Indexing, Selection, and Filtering](#indexing-selection-and-filtering)

   * [Label-based (`.loc`)](#label-based-loc)
   * [Position-based (`.iloc`)](#position-based-iloc)
   * [Mixed (`.at`, `.iat`)](#mixed-at-iat)
   * [Boolean Indexing / Filtering](#boolean-indexing--filtering)
   * [SettingWithCopy Warning](#settingwithcopy-warning)
8. [Operating on DataFrames](#operating-on-dataframes)

   * [Column Operations](#column-operations)
   * [Row Operations](#row-operations)
   * [Elementwise Operations & Vectorized Functions](#elementwise-operations--vectorized-functions)
   * [Applying Functions (`apply`, `map`, `applymap`)](#applying-functions-apply-map-applymap)
   * [Aggregation and Grouping (`groupby`)](#aggregation-and-grouping-groupby)
   * [Sorting (`sort_values`, `sort_index`)](#sorting-sort_values-sort_index)
9. [Handling Missing Data](#handling-missing-data)

   * [Detecting Missing Values](#detecting-missing-values)
   * [Dropping Missing Data](#dropping-missing-data)
   * [Filling Missing Data](#filling-missing-data)
   * [Interpolation](#interpolation)
10. [Combining and Merging Datasets](#combining-and-merging-datasets)

    * [Concatenation (`pd.concat`)](#concatenation-pdconcat)
    * [Merging / Joining (`pd.merge`, `.join`)](#merging--joining-pdmerge-join)
    * [Appending Rows](#appending-rows)
    * [Database-style Joins](#database-style-joins)
11. [Reshaping Data](#reshaping-data)

    * [Pivot Tables (`pivot`, `pivot_table`)](#pivot-tables-pivot-pivot_table)
    * [Stack / Unstack](#stack--unstack)
    * [Melt](#melt)
    * [Wide-to-Long and Long-to-Wide Transformations](#wide-to-long-and-long-to-wide-transformations)
12. [Time Series Functionality](#time-series-functionality)

    * [Datetime Index](#datetime-index)
    * [Resampling](#resampling)
    * [Rolling, Expanding, EWM](#rolling-expanding-ewm)
    * [Time Zone Handling](#time-zone-handling)
    * [Period and Interval](#period-and-interval)
13. [Input/Output (I/O)](#inputoutput-io)

    * [CSV / TXT](#csv--txt)
    * [Excel](#excel)
    * [JSON](#json)
    * [HTML](#html)
    * [SQL Databases](#sql-databases)
    * [Pickle / Feather / Parquet](#pickle--feather--parquet)
14. [Performance Tips and Best Practices](#performance-tips-and-best-practices)

    * [Vectorization](#vectorization)
    * [Avoiding Loops](#avoiding-loops)
    * [Categorical dtype](#categorical-dtype)
    * [Memory Usage](#memory-usage)
    * [Chunking Large Data](#chunking-large-data)
    * [Using `eval` / `query`](#using-eval--query)
    * [Parallelization Options](#parallelization-options)
15. [Visualization Integration](#visualization-integration)

    * [Matplotlib Integration](#matplotlib-integration)
    * [Seaborn / Other Libraries](#seaborn--other-libraries)
16. [Interoperability with Other Libraries](#interoperability-with-other-libraries)
17. [Common Pitfalls and FAQs](#common-pitfalls-and-faqs)
18. [Example Workflow](#example-workflow)
19. [Further Resources](#further-resources)

---

## Introduction

pandas is a powerful open-source Python library providing data structures and data analysis tools, primarily:

* **Series**: 1D labeled array capable of holding any data type.
* **DataFrame**: 2D labeled data structure with columns of potentially different types (like a table or spreadsheet).

pandas builds on NumPy to offer easy-to-use, high-performance data manipulation.

---

## Installation

Install via pip or conda:

```bash
pip install pandas
```

Or with conda:

```bash
conda install pandas
```

pandas depends on NumPy; installing pandas will install NumPy if not already present.

---

## Importing pandas

```python
import pandas as pd
```

By convention, `pd` is used as the alias.

---

## Core Data Structures

### Series

* 1D labeled homogeneous array.
* Has an index (labels) and values.
* Can hold any data type (ints, floats, strings, Python objects, etc.).

Example:

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# a    10
# b    20
# c    30
# dtype: int64
```

### DataFrame

* 2D labeled data structure with columns of potentially different types.
* Think of it like a spreadsheet or SQL table.
* Index for rows, columns have labels as well.

Example:

```python
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 22],
    'score': [85.5, 92.0, 88.0]
}
df = pd.DataFrame(data)
print(df)
#       name  age  score
# 0    Alice   25   85.5
# 1      Bob   30   92.0
# 2  Charlie   22   88.0
```

---

## Creating Series and DataFrames

### From Python Structures

* **Series**: from list, dict, scalar.

  ```python
  # From list with default index
  s1 = pd.Series([1, 2, 3])
  # From list with custom index
  s2 = pd.Series([1, 2, 3], index=['x', 'y', 'z'])
  # From dict: keys become index
  s3 = pd.Series({'x': 10, 'y': 20, 'z': 30})
  # From scalar: repeats scalar with given index
  s4 = pd.Series(5, index=['a', 'b', 'c'])
  ```
* **DataFrame**: from dict of equal-length lists/arrays/Series, list of dicts, list of lists with columns specified.

  ```python
  # From dict of lists
  df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
  # From list of dicts
  rows = [{'A': 1, 'B': 4}, {'A': 2, 'B': 5}, {'A': 3, 'B': 6}]
  df2 = pd.DataFrame(rows)
  # From list of lists with columns
  data = [[1, 4], [2, 5], [3, 6]]
  df3 = pd.DataFrame(data, columns=['A', 'B'])
  ```

### From NumPy Arrays

* Convert array to Series or DataFrame; specify index/columns:

  ```python
  import numpy as np
  arr = np.random.randn(5)
  s = pd.Series(arr, index=pd.date_range('2025-01-01', periods=5))
  arr2d = np.random.randn(4, 3)
  df = pd.DataFrame(arr2d, columns=['col1', 'col2', 'col3'])
  ```

### From Dictionaries

* Nested dicts can create DataFrame: outer keys become columns, inner keys become row indices.

  ```python
  data = {
      'A': {'x': 1, 'y': 2},
      'B': {'x': 3, 'y': 4}
  }
  df = pd.DataFrame(data)
  #       A  B
  # x     1  3
  # y     2  4
  ```

### From External Files or Databases

* See [I/O section](#inputoutput-io) below for details on reading from CSV, Excel, SQL, JSON, etc.

---

## Inspecting Data

### Viewing Top/Bottom Rows

```python
df.head()    # first 5 rows by default
df.head(10)  # first 10 rows
df.tail()    # last 5 rows
```

### Information and Summary Statistics

```python
df.info()      # index dtype, column dtypes, non-null counts, memory usage
df.describe()  # summary statistics for numeric columns (count, mean, std, min, quartiles, max)
df.describe(include=['object', 'category'])  # summary for object/categorical columns
df.value_counts()  # for a Series: counts of unique values
```

### DataFrame Attributes

* `df.shape`: tuple (n\_rows, n\_columns)
* `df.columns`: Index of column labels
* `df.index`: Index of row labels
* `df.dtypes`: Series with column dtypes
* `df.size`: total number of elements (n\_rows \* n\_columns)
* `df.values`: underlying NumPy array (may be heterogeneous dtype=object)
* `df.memory_usage(deep=True)`: memory usage per column

Example:

```python
print(df.shape)      # e.g., (1000, 5)
print(df.columns)    # Index([...], dtype='object')
```

---

## Indexing, Selection, and Filtering

### Label-based (`.loc`)

* Access rows and columns by labels.
* Syntax: `df.loc[row_label, col_label]`
* Single label, list of labels, slice of labels, boolean mask.

Examples:

```python
# Assume df has index ['a','b','c'] and columns ['x','y','z']
df.loc['a']            # Series: row 'a'
df.loc[['a', 'c'], ['x', 'z']]  # DataFrame with specified rows and columns
df.loc['a':'c', :]     # rows from 'a' to 'c' inclusive, all columns
df.loc[:, ['x', 'y']]  # all rows, columns x and y
```

### Position-based (`.iloc`)

* Access by integer location (0-based).
* Syntax: `df.iloc[row_idx, col_idx]`

Examples:

```python
df.iloc[0]             # first row
df.iloc[0:3, 1:4]      # rows 0-2, columns 1-3
df.iloc[[0, 2], [1, 3]] # specific positions
```

### Mixed (`.at`, `.iat`)

* `.at[row_label, col_label]`: fast scalar access by label.
* `.iat[row_idx, col_idx]`: fast scalar access by integer position.

```python
val = df.at['row_label', 'col_label']
val2 = df.iat[0, 1]
```

### Boolean Indexing / Filtering

* Filter rows based on condition(s).

```python
# Single condition
df_filtered = df[df['age'] > 30]
# Multiple conditions: use & (and), | (or), ~ (not) with parentheses
mask = (df['age'] > 20) & (df['score'] >= 80)
df2 = df[mask]

# Filtering with isin
df3 = df[df['category'].isin(['A', 'B'])]

# Filtering strings: str methods
df[df['name'].str.contains('Alice')]
```

### SettingWithCopy Warning

* Occurs when pandas isn’t sure if you are modifying a copy or the original. To avoid:

  * Use `.loc` for assignment: `df.loc[mask, 'col'] = new_value`.
  * Avoid chained indexing like `df[df['A'] > 0]['B'] = ...`.
  * If needed, make an explicit copy: `df2 = df[mask].copy()` then modify `df2`.

Example:

```python
# Correct:
mask = df['age'] < 25
df.loc[mask, 'score'] = 0
# Avoid:
df[df['age'] < 25]['score'] = 0  # may raise SettingWithCopyWarning
```

---

## Operating on DataFrames

### Column Operations

* Select a column: `df['col']` or `df.col` (latter only if column name is a valid attribute and no conflict).
* Create or modify: `df['new_col'] = ...`.
* Drop column: `df.drop('col', axis=1)` or `df.drop(columns=['col1','col2'])`.

Examples:

```python
df['total'] = df['math'] + df['english']
df = df.drop(columns=['unnecessary_col'])
```

### Row Operations

* Select row by index: `df.loc[row_label]` or `df.iloc[row_idx]`.
* Add a new row: often via `pd.concat` or `df.append` (deprecated in newer pandas; use `pd.concat([df, new_row_df])`).
* Drop rows: `df.drop(index=['row1', 'row2'])` or `df.drop(index=integer_index)`.

Example:

```python
# Drop row with label 'a'
df2 = df.drop(index='a')
```

### Elementwise Operations & Vectorized Functions

* Arithmetic on columns/Series: `df['col'] * 2`, or between columns: `df['A'] + df['B']`.
* Use NumPy ufuncs: `np.log(df['value'])`, `df['value'].apply(np.sqrt)` (but direct ufunc often faster: `np.sqrt(df['value'])`).
* Broadcasting: operations align on index; missing labels produce NaN.

Example:

```python
df['log_score'] = np.log(df['score'] + 1)
```

### Applying Functions (`apply`, `map`, `applymap`)

* **`Series.map`**: map values in a Series via dict or function.

  ```python
  df['grade'] = df['score'].map(lambda x: 'pass' if x>=50 else 'fail')
  ```
* **`Series.apply`**: apply a function elementwise, can return scalar or sequence.

  ```python
  df['adjusted'] = df['score'].apply(lambda x: x*1.1)
  ```
* **`DataFrame.apply`**: apply function along axis (rows or columns).

  ```python
  # Sum across columns for each row:
  df['row_sum'] = df.apply(lambda row: row['A'] + row['B'] + row['C'], axis=1)
  ```
* **`DataFrame.applymap`**: apply function elementwise across entire DataFrame.

  ```python
  df2 = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
  ```

Use vectorized operations or built-in methods where possible, as they are faster than Python-level apply.

### Aggregation and Grouping (`groupby`)

* Split data into groups based on column(s), then apply aggregation or transformation.
* Syntax: `df.groupby('col')`, `df.groupby(['col1','col2'])`.
* After grouping, methods like `.sum()`, `.mean()`, `.agg()`, `.apply()`, `.transform()`, `.filter()`.
* Example:

  ```python
  grouped = df.groupby('category')
  summary = grouped['sales'].agg(['sum', 'mean', 'count'])
  # Or multiple aggregations on multiple columns:
  df.groupby(['region', 'product'])['sales', 'profit'].agg({'sales':'sum', 'profit':'mean'})
  ```
* Using `.transform` to return aligned shape:

  ```python
  df['sales_zscore'] = grouped['sales'].transform(lambda x: (x - x.mean()) / x.std())
  ```
* Filtering groups:

  ```python
  # Keep groups where total sales > threshold
  df_filtered = grouped.filter(lambda x: x['sales'].sum() > 1000)
  ```

### Sorting (`sort_values`, `sort_index`)

* Sort by column values:

  ```python
  df_sorted = df.sort_values(by='score', ascending=False)
  # Multiple columns:
  df.sort_values(by=['category','score'], ascending=[True, False])
  ```
* Sort by index:

  ```python
  df.sort_index(axis=0)   # sort rows by index
  df.sort_index(axis=1)   # sort columns by column labels
  ```
* In-place sorting: pass `inplace=True`.

Example:

```python
df.sort_values('date', inplace=True)
```

---

## Handling Missing Data

### Detecting Missing Values

* pandas uses `NaN` (float) or `None` for missing data.
* Methods:

  ```python
  df.isna()      # DataFrame of booleans
  df.isnull()    # same as isna()
  df.notna()     # inverse
  df['col'].isna().sum()   # count missing in a column
  ```

### Dropping Missing Data

* `df.dropna()`: drop rows with any missing by default.
* Parameters:

  * `axis=0` (rows) or `axis=1` (columns).
  * `how='any'` (default) drops if any NaN, `how='all'` drops if all values are NaN.
  * `thresh`: require a minimum number of non-NA values.
  * `subset`: specify columns to consider.
* Example:

  ```python
  df_clean = df.dropna(subset=['col1','col2'], how='any')
  df2 = df.dropna(axis=1, how='all')  # drop columns entirely empty
  ```

### Filling Missing Data

* `df.fillna(value, method=None, axis=None, inplace=False, limit=None)`

  * `value`: scalar or dict mapping column to fill value.
  * `method='ffill'` (forward-fill), `'bfill'` (backward-fill).
  * `limit`: max consecutive NaNs to fill.
* Example:

  ```python
  df_filled = df.fillna(0)
  df['col'] = df['col'].fillna(df['col'].mean())
  df_ffill = df.fillna(method='ffill')
  ```

### Interpolation

* `df.interpolate(method='linear', axis=0, limit_direction='forward')`
* Useful for time series:

  ```python
  df_time = df.set_index('date').sort_index()
  df_time['value_interp'] = df_time['value'].interpolate(method='time')
  ```

---

## Combining and Merging Datasets

### Concatenation (`pd.concat`)

* Stack DataFrames along rows or columns.
* `pd.concat([df1, df2, ...], axis=0 or 1, ignore_index=False, keys=None, join='outer'/'inner')`
* Example:

  ```python
  df_all = pd.concat([df_jan, df_feb, df_mar], axis=0, ignore_index=True)
  # For columns:
  df_wide = pd.concat([df_left, df_right], axis=1)
  ```
* `join='outer'` keeps all columns; `join='inner'` keeps only intersection.

### Merging / Joining (`pd.merge`, `.join`)

* SQL-style joins on key columns or index.
* `pd.merge(left, right, how='inner'/'left'/'right'/'outer', on='key', left_on=..., right_on=..., suffixes=('_x','_y'))`
* Examples:

  ```python
  merged = pd.merge(df_customers, df_orders, how='left', on='customer_id')
  ```
* `.join`: join on index by default:

  ```python
  df1.join(df2, how='inner')  # aligns on index
  ```

### Appending Rows

* `df.append(...)` is deprecated; instead, use `pd.concat`.
* Example:

  ```python
  new_row = pd.DataFrame({'A':[10], 'B':[20]})
  df = pd.concat([df, new_row], ignore_index=True)
  ```

### Database-style Joins

* Inner: only matching keys.
* Left: all left keys, matching right or NaN.
* Right: all right keys.
* Outer: union of keys, missing filled with NaN.

---

## Reshaping Data

### Pivot Tables (`pivot`, `pivot_table`)

* **`pivot`**: reshape using unique index/column combinations; raises error if duplicates.

  ```python
  df_pivot = df.pivot(index='date', columns='category', values='sales')
  ```
* **`pivot_table`**: allows aggregation if duplicates exist; parameters: `index`, `columns`, `values`, `aggfunc`, `fill_value`, `margins`.

  ```python
  pt = df.pivot_table(index='region', columns='product', values='sales', aggfunc='sum', fill_value=0, margins=True)
  ```

### Stack / Unstack

* `stack`: pivot columns into index (long format).
* `unstack`: inverse: pivot index level into columns.

  ```python
  df2 = df_multiindex.unstack(level='category')
  df_long = df2.stack()
  ```

### Melt

* Convert wide format to long format.

  ```python
  df_melted = pd.melt(df, id_vars=['id', 'date'], value_vars=['var1','var2'], var_name='variable', value_name='value')
  ```

### Wide-to-Long and Long-to-Wide Transformations

* Tools like `pd.wide_to_long` for structured wide-to-long.
* Combined with multi-index can handle complex reshaping.

---

## Time Series Functionality

### Datetime Index

* Convert column to datetime: `pd.to_datetime(df['date'])`.
* Set as index: `df.set_index('date', inplace=True)`.
* Ensure sorted index: `df.sort_index(inplace=True)`.
* Access via index: `df.loc['2025-01-01']`, `df.loc['2025-01':'2025-03']`.

Example:

```python
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
```

### Resampling

* Change frequency: `df.resample('M').agg({'sales':'sum'})` for monthly sum.
* Common offsets: ‘D’ (day), ‘W’, ‘M’, ‘Q’, ‘A’, ‘H’, etc.
* Downsampling (e.g., daily→monthly) or upsampling with fill/interpolation.

  ```python
  monthly = df.resample('M').mean()
  daily = df.resample('D').ffill()
  ```

### Rolling, Expanding, EWM

* **Rolling window**: `df['value'].rolling(window=3).mean()`
* **Expanding window**: cumulative: `df['value'].expanding().sum()`
* **Exponentially weighted**: `df['value'].ewm(span=5).mean()`

Example:

```python
df['rolling_mean_7'] = df['value'].rolling(window=7).mean()
df['ewm_5'] = df['value'].ewm(span=5).mean()
```

### Time Zone Handling

* Localize naive datetimes: `df.index = df.index.tz_localize('UTC')`
* Convert to other zones: `df.index = df.index.tz_convert('Asia/Kolkata')`
* Careful when arithmetic across time zones.

### Period and Interval

* `pd.Period`: represents period (e.g., month, quarter).
* `df_period = df.to_period('M')`
* IntervalIndex for intervals.

---

## Input/Output (I/O)

### CSV / TXT

* Read CSV: `pd.read_csv('file.csv', sep=',', header=0, index_col=None, parse_dates=['date_col'], dtype={'col': type}, na_values=['NA'], chunksize=... )`.
* Write CSV: `df.to_csv('out.csv', index=True/False)`.
* For large files: consider `chunksize` in `read_csv` to iterate.

Example:

```python
df = pd.read_csv('data.csv', parse_dates=['date'])
df.to_csv('data_out.csv', index=False)
```

### Excel

* Read: `pd.read_excel('file.xlsx', sheet_name='Sheet1', usecols=['A','B'], parse_dates=['date'])`.
* Write: `df.to_excel('out.xlsx', sheet_name='Sheet1', index=False)`.
* Requires `openpyxl` or `xlrd` depending on file type.

### JSON

* Read: `pd.read_json('data.json', orient='records')`; supports various orientations.
* Write: `df.to_json('out.json', orient='records', date_format='iso')`.

### HTML

* Read tables from HTML pages: `pd.read_html('http://example.com/page.html')` returns list of DataFrames.
* Write: `df.to_html('out.html')`.

### SQL Databases

* Use SQLAlchemy engine.

  ```python
  from sqlalchemy import create_engine
  engine = create_engine('sqlite:///mydb.sqlite')
  df = pd.read_sql('SELECT * FROM table_name', con=engine)
  df.to_sql('new_table', con=engine, if_exists='replace', index=False)
  ```

### Pickle / Feather / Parquet

* **Pickle**: `df.to_pickle('df.pkl')`, `pd.read_pickle('df.pkl')` (Python-specific, not cross-language).
* **Feather**: `df.to_feather('df.feather')`, `pd.read_feather('df.feather')` (fast, columnar).
* **Parquet**: `df.to_parquet('df.parquet')`, `pd.read_parquet('df.parquet')` (efficient, compressed, good for large data).
* Choose based on performance, interoperability, compression needs.

---

## Performance Tips and Best Practices

### Vectorization

* Use built-in vectorized operations rather than Python loops.
* Example: `df['C'] = df['A'] + df['B']` instead of row-wise loop.

### Avoiding Loops

* Avoid iterating rows with `for index, row in df.iterrows()` for large datasets; it’s slow.
* If needed, use vectorized `.apply` sparingly, or consider Cython/Numba for heavy custom operations.

### Categorical dtype

* Convert string columns with limited unique values to `category` dtype to save memory and speed up groupby/sorting.

  ```python
  df['category'] = df['category'].astype('category')
  ```

### Memory Usage

* Assess: `df.info(memory_usage='deep')`.
* Downcast numeric types if possible: `pd.to_numeric(df['col'], downcast='integer')`.
* Drop unused columns early.
* For very large data, consider chunking or using Dask.

### Chunking Large Data

* Read large CSVs in chunks: `for chunk in pd.read_csv('large.csv', chunksize=100000): process(chunk)`.
* Aggregate results incrementally to avoid loading entire file into memory.

### Using `eval` / `query`

* For large DataFrames, `df.eval("C = A + B")` or `df.query("A > 0 and B < 5")` can be faster and use less memory, as pandas can optimize under the hood.

  ```python
  df = df.eval("total = price * quantity")
  df_filtered = df.query("total > 1000")
  ```

### Parallelization Options

* pandas itself is mostly single-threaded; some operations (like groupby with certain backends) may use multiple cores.
* For heavier workloads, consider:

  * Dask DataFrame for out-of-core and parallel computations with pandas-like API.
  * Modin as a drop-in pandas acceleration.
  * Swifter for faster `apply` where possible.
  * Use vectorized NumPy or specialized libraries.

---

## Visualization Integration

### Matplotlib Integration

* pandas methods often wrap matplotlib (requires `import matplotlib.pyplot as plt`).
* Quick plots:

  ```python
  df['value'].plot(kind='line')       # line plot
  df.plot(x='date', y='value', kind='scatter')
  df.plot(kind='hist', bins=20)
  plt.show()
  ```
* For multiple series:

  ```python
  df[['A','B']].plot(kind='line')
  ```

### Seaborn / Other Libraries

* Convert DataFrame to arrays or pass DataFrame and column names.

  ```python
  import seaborn as sns
  sns.scatterplot(data=df, x='feature1', y='feature2', hue='category')
  ```
* Use pandas for data preparation, then feed into specialized plotting libraries (Matplotlib, Seaborn, Plotly, Altair, etc.).

---

## Interoperability with Other Libraries

* **NumPy**: pandas Series/DataFrame values are often NumPy arrays; use NumPy functions on them.
* **SciPy**: for statistical or scientific computations on arrays extracted from DataFrame.
* **scikit-learn**: expect arrays or DataFrames; you can pass `.values` or DataFrame directly (many accept DataFrame with column names).
* **SQLAlchemy**: for database read/write.
* **Dask / Modin**: scale pandas workflows.
* **PySpark**: for big data, but pandas is often used for smaller samples or local testing.
* **Visualization**: matplotlib, seaborn, plotly, etc.
* **Machine Learning / Deep Learning**: convert DataFrame to arrays or tensors (`.values`, `torch.from_numpy`).
* **Excel / BI Tools**: pandas can export to formats that BI tools can ingest.

---

## Common Pitfalls and FAQs

1. **Chained indexing and SettingWithCopyWarning**

   * Avoid ambiguous chained operations. Use `.loc` to assign.

2. **Mixed types within columns**

   * A column with mixed types may be dtype `object`, hurting performance. Convert to uniform types when possible.

3. **Datetime parsing**

   * Always parse date columns explicitly via `parse_dates` or `pd.to_datetime`. Beware of inconsistent date formats.

4. **Index alignment**

   * Operations between Series/DataFrames align on index labels; mismatched indexes produce NaN. To avoid, reset index or reindex appropriately.

5. **Modifying slices vs copies**

   * Understand when operations return views vs copies. When in doubt, use `.copy()`.

6. **Large dataset memory**

   * pandas is in-memory; for data larger than RAM, use chunking or libraries like Dask.

7. **Merging with duplicate keys**

   * Be aware that merges can produce more rows than original if keys are not unique. Check keys’ uniqueness or handle using aggregation.

8. **Groupby performance**

   * For extremely large data, groupby can be slow. Consider categoricals, or alternative libraries.

9. **Categorical pitfalls**

   * When adding new categories not seen during `.astype('category')`, pandas may treat them as NaN unless categories are updated.

10. **Reading large files**

    * Use appropriate arguments: `dtype`, `usecols`, `nrows`, `chunksize`, `low_memory=False`, to speed up and reduce memory.

11. **Invisible floats precision**

    * When displaying DataFrame, pandas may truncate floats; set display options if needed:

      ```python
      pd.set_option('display.precision', 3)
      pd.set_option('display.max_rows', 100)
      pd.set_option('display.max_columns', 20)
      ```

12. **Datetime arithmetic**

    * After operations, ensure the result’s dtype is datetime if needed; use `pd.to_datetime` on results.

13. **Avoid `apply` when vectorized exists**

    * Many operations (string methods, datetime methods, arithmetic) are vectorized; prefer them over `apply`.

14. **Version compatibility**

    * pandas APIs evolve; check version-specific docs if using older/newer versions.

---

## Example Workflow

Below is a small illustrative example showing a typical data analysis workflow in pandas: reading data, cleaning, feature engineering, analysis, and export.

```python
import pandas as pd
import numpy as np

# 1. Read data
df = pd.read_csv('sales_data.csv', parse_dates=['date'])

# 2. Inspect
print(df.head())
print(df.info())
print(df.describe())

# 3. Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 4. Handle missing data
# Suppose 'sales' has missing:
df['sales'] = df['sales'].fillna(0)
# For 'region', fill with 'Unknown'
df['region'] = df['region'].fillna('Unknown')

# 5. Feature engineering
# Create month, year from date
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
# Create sales per unit if quantity column exists
df['sales_per_unit'] = df['sales'] / df['quantity']

# 6. Filter data
df = df[df['sales'] > 0]

# 7. Aggregation: monthly sales per region
monthly = df.groupby(['region', 'year', 'month'])['sales'].sum().reset_index()
monthly = monthly.sort_values(['region', 'year', 'month'])

# 8. Pivot for reporting
report = monthly.pivot_table(index=['region','year'], columns='month', values='sales', aggfunc='sum', fill_value=0)
# Rename columns from numbers to month names if desired
report.columns = [f'month_{m}' for m in report.columns]

# 9. Add cumulative annual sales
report['annual_sales'] = report.sum(axis=1)

# 10. Merge with region metadata (e.g., target quotas)
region_meta = pd.read_excel('region_meta.xlsx')  # has columns 'region', 'quota'
report = report.reset_index().merge(region_meta, on='region', how='left')

# 11. Calculate performance vs quota
report['achievement_pct'] = report['annual_sales'] / report['quota'] * 100

# 12. Sort and inspect top performers
top = report.sort_values('achievement_pct', ascending=False).head(10)
print(top)

# 13. Export results
report.to_csv('annual_region_report.csv', index=False)
```

This workflow demonstrates:

* Reading and writing various formats.
* Cleaning and transforming column names.
* Handling missing values.
* Date/time feature extraction.
* Grouping and aggregation.
* Pivoting for summary tables.
* Merging additional metadata.
* Calculations and export.

---

## Further Resources

* Official pandas Documentation:
  [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
* User Guide:
  [https://pandas.pydata.org/docs/user\_guide/index.html](https://pandas.pydata.org/docs/user_guide/index.html)
* Tutorials:

  * “10 Minutes to pandas” in the official docs.
  * pandas Cookbook and online tutorials (e.g., DataCamp, Real Python).
* Books:

  * “Python for Data Analysis” by Wes McKinney.
  * “Effective Pandas” by Matt Harrison.
* Community:

  * Stack Overflow for specific questions.
  * pandas GitHub issues for bug reports and discussions.

---

> **Usage Tips**:
>
> * Experiment interactively in Jupyter notebooks for immediate feedback.
> * Profile operations on large data: test on subsets before scaling up.
> * Keep pandas up to date to benefit from performance improvements and new features.
> * When working with very large datasets, evaluate whether pandas alone suffices or if tools like Dask/Modin are needed.

---

