
## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Importing NumPy](#importing-numpy)
4. [Creating Arrays](#creating-arrays)

   * [From Python Sequences](#from-python-sequences)
   * [Using NumPy Functions](#using-numpy-functions)
   * [Special Arrays](#special-arrays)
5. [Array Attributes](#array-attributes)
6. [Indexing and Slicing](#indexing-and-slicing)

   * [Basic Indexing](#basic-indexing)
   * [Slicing](#slicing)
   * [Fancy Indexing](#fancy-indexing)
   * [Boolean Masking](#boolean-masking)
7. [Array Operations](#array-operations)

   * [Elementwise Operations](#elementwise-operations)
   * [Universal Functions (ufuncs)](#universal-functions-ufuncs)
   * [Aggregations / Reductions](#aggregations--reductions)
   * [Broadcasting](#broadcasting)
8. [Reshaping and Resizing](#reshaping-and-resizing)

   * [Reshape, Resize, Flatten](#reshape-resize-flatten)
   * [Transpose and Axes Manipulation](#transpose-and-axes-manipulation)
9. [Stacking and Splitting Arrays](#stacking-and-splitting-arrays)

   * [Concatenation / Stacking](#concatenation--stacking)
   * [Splitting](#splitting)
10. [Mathematical and Statistical Functions](#mathematical-and-statistical-functions)

    * [Basic Math](#basic-math)
    * [Statistics](#statistics)
    * [Linear Algebra](#linear-algebra)
    * [Random Number Generation](#random-number-generation)
11. [Input/Output](#inputoutput)

    * [Saving and Loading `.npy` / `.npz`](#saving-and-loading-npy--npz)
    * [Text Files (CSV, TXT)](#text-files-csv-txt)
12. [Structured and Record Arrays](#structured-and-record-arrays)
13. [Performance Tips and Best Practices](#performance-tips-and-best-practices)
14. [Interoperability with Other Libraries](#interoperability-with-other-libraries)
15. [Common Pitfalls and FAQs](#common-pitfalls-and-faqs)
16. [Further Resources](#further-resources)

---

## Introduction

NumPy (Numerical Python) is the foundational package for numerical computing in Python. It provides:

* A powerful N-dimensional array object (`ndarray`).
* Fast operations on arrays (vectorized operations).
* Tools for integrating C/C++ and Fortran code.
* Linear algebra, random number generation, and more.

Using NumPy arrays instead of Python lists leads to more efficient storage and faster computation, especially for large datasets.

---

## Installation

To install NumPy, use pip or conda:

```bash
pip install numpy
```

Or with conda:

```bash
conda install numpy
```

---

## Importing NumPy

```python
import numpy as np
```

By convention, `np` is used as the alias.

---

## Creating Arrays

### From Python Sequences

You can create arrays from lists or tuples:

```python
import numpy as np

# 1D array
a = np.array([1, 2, 3, 4])
print(a)           # [1 2 3 4]
print(type(a))     # <class 'numpy.ndarray'>

# 2D array (list of lists)
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat)
# [[1 2 3]
#  [4 5 6]]
```

* All elements in the array must be of the same data type; NumPy will upcast if needed (e.g., mixing ints and floats yields floats).

### Using NumPy Functions

NumPy provides functions to create arrays without explicitly listing elements.

* `np.arange(start, stop, step)`: like Python’s `range`, but returns an array.

  ```python
  arr = np.arange(0, 10, 2)   # [0 2 4 6 8]
  ```
* `np.linspace(start, stop, num)`: returns `num` evenly spaced samples from `start` to `stop` inclusive.

  ```python
  arr = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]
  ```
* `np.logspace(start, stop, num, base=10.0)`: logarithmically spaced.

  ```python
  arr = np.logspace(0, 3, 4)  # [1.e+00, 1.e+01, 1.e+02, 1.e+03]
  ```
* `np.random.*`: e.g., `np.random.rand`, `np.random.randn`, `np.random.randint`, etc., for random arrays.

### Special Arrays

* `np.zeros(shape, dtype=float)`: array of zeros.

  ```python
  z = np.zeros((2, 3))    # 2x3 array of 0.0
  ```
* `np.ones(shape, dtype=float)`: array of ones.

  ```python
  o = np.ones((3, 2))     # 3x2 array of 1.0
  ```
* `np.eye(N, M=None, k=0)`: identity matrix (2D).

  ```python
  I = np.eye(3)           # 3x3 identity
  ```
* `np.full(shape, fill_value)`: array filled with specified value.

  ```python
  f = np.full((2, 2), 7)  # [[7,7],[7,7]]
  ```
* `np.empty(shape)`: uninitialized array (contents arbitrary). Useful when you plan to overwrite all entries.
* `np.repeat` and `np.tile`: repeat elements or tile arrays.

  ```python
  x = np.array([1, 2, 3])
  np.repeat(x, 2)         # [1 1 2 2 3 3]
  np.tile(x, 2)           # [1 2 3 1 2 3]
  ```

---

## Array Attributes

Given an array `arr`, key attributes:

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
```

* `arr.shape`: tuple of array dimensions.

  ```python
  print(arr.shape)  # (2, 3)
  ```
* `arr.ndim`: number of dimensions (axes).

  ```python
  print(arr.ndim)   # 2
  ```
* `arr.size`: total number of elements (product of shape).

  ```python
  print(arr.size)   # 6
  ```
* `arr.dtype`: data type of elements (e.g., `int64`, `float64`).

  ```python
  print(arr.dtype)  # dtype('int64') or similar
  ```
* `arr.itemsize`: size in bytes of each element.

  ```python
  print(arr.itemsize)  # e.g., 8 bytes for int64
  ```
* `arr.data`: buffer object pointing to the array’s data (rarely used directly).

---

## Indexing and Slicing

### Basic Indexing

* 1D arrays:

  ```python
  a = np.array([10, 20, 30, 40, 50])
  print(a[0])    # 10
  print(a[-1])   # 50 (last element)
  ```
* 2D arrays:

  ```python
  mat = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
  print(mat[0, 1])  # 2 (row 0, col 1)
  print(mat[2, -1]) # 9
  ```
  ```python
  mat = np.array([[[1], [2], [3]],
                  [[1], [2], [3]],
                  [[1], [2], [3]]])
  print(mat[0, 1])  # 2 (row 0, col 1)
  print(mat[2, -1]) # 9
  ```
* Higher dimensions: use a comma-separated index for each axis.

### Slicing

* Similar to Python lists, but for each dimension:

  ```python
  a = np.arange(10)         # [0 1 2 3 4 5 6 7 8 9]
  print(a[2:7])             # [2 3 4 5 6]
  print(a[:5])              # [0 1 2 3 4]
  print(a[5:])              # [5 6 7 8 9]
  print(a[::2])             # [0 2 4 6 8] (step 2)
  ```
* 2D slicing:

  ```python
  mat = np.arange(16).reshape((4, 4))
  # [[ 0  1  2  3]
  #  [ 4  5  6  7]
  #  [ 8  9 10 11]
  #  [12 13 14 15]]

  print(mat[1:3, 2:4])
  # [[ 6  7]
  #  [10 11]]

  print(mat[:, 1])   # all rows, column 1: [1,5,9,13]
  print(mat[2, :])   # row 2 all columns: [8,9,10,11]
  ```
* Note: slicing returns a **view** (when possible), not a copy. Modifying the slice may modify the original array.

### Fancy Indexing

* Integer array indexing:

  ```python
  arr = np.array([0, 10, 20, 30, 40])
  idx = np.array([1, 3, 4])
  print(arr[idx])   # [10 30 40]
  ```
* Multi-dimensional:

  ```python
  mat = np.arange(9).reshape((3,3))
  rows = np.array([0, 2])
  cols = np.array([1, 2])
  # This selects elements at (0,1) and (2,2)
  print(mat[rows, cols])   # [1 8]
  ```
* Fancy indexing always returns a copy.

### Boolean Masking

* Create a boolean mask and use it to filter:

  ```python
  a = np.array([1, 2, 3, 4, 5])
  mask = a > 2
  print(mask)      # [False False  True  True  True]
  print(a[mask])   # [3 4 5]
  ```
* Combined conditions: use bitwise operators `&`, `|`, `~` with parentheses:

  ```python
  a = np.arange(10)
  cond = (a % 2 == 0) & (a > 3)   # even numbers greater than 3
  print(a[cond])                  # [4 6 8]
  ```

---

## Array Operations

### Elementwise Operations

* Arithmetic operations apply elementwise:

  ```python
  a = np.array([1, 2, 3])
  b = np.array([4, 5, 6])
  print(a + b)    # [5 7 9]
  print(a - b)    # [-3 -3 -3]
  print(a * b)    # [4 10 18]
  print(a / b)    # [0.25 0.4  0.5 ]
  print(a ** 2)   # [1 4 9]
  ```
* Broadcasting rules apply when shapes differ (see Broadcasting section).

### Universal Functions (ufuncs)

NumPy provides many vectorized functions:

```python
a = np.array([0, np.pi/2, np.pi])
print(np.sin(a))    # [0.0, 1.0, 0.0]
print(np.exp(a))    # [1.         4.81047738 23.14069263]
print(np.log(a + 1)) # avoid log(0)
```

Common ufuncs: `sin, cos, tan, exp, log, sqrt, abs, minimum, maximum`, etc.

### Aggregations / Reductions

* Sum, mean, min, max, etc., over entire array or along axes:

  ```python
  mat = np.array([[1, 2, 3],
                  [4, 5, 6]])
  print(mat.sum())          # 21
  print(mat.sum(axis=0))    # [5 7 9] column-wise
  print(mat.sum(axis=1))    # [6 15] row-wise
  print(mat.mean())         # 3.5
  print(mat.min(), mat.max()) # 1, 6
  print(mat.std(), mat.var()) # standard deviation, variance
  ```
* Other reduction functions: `np.prod`, `np.cumprod`, `np.cumsum`, `np.all`, `np.any`, etc.

### Broadcasting

* Allows operations on arrays of different shapes by “stretching” smaller arrays along dimensions of size 1.
* Rules: two dimensions are compatible if they are equal or one of them is 1. NumPy expands dimensions of size 1 to match.
* Example:

  ```python
  A = np.array([[1,2,3],[4,5,6]])   # shape (2,3)
  b = np.array([10, 20, 30])        # shape (3,)
  # b is broadcast across rows:
  print(A + b)
  # [[11 22 33]
  #  [14 25 36]]
  ```
* Column vector plus row vector:

  ```python
  col = np.array([[1], [2], [3]])  # shape (3,1)
  row = np.array([10, 20, 30])     # shape (3,)
  # col + row: shapes (3,1) and (3,) -> broadcast to (3,3)
  print(col + row)
  # [[11 21 31]
  #  [12 22 32]
  #  [13 23 33]]
  ```
* Use broadcasting to avoid explicit loops; it’s efficient in C-backed implementation.

---

## Reshaping and Resizing

### Reshape, Resize, Flatten

* `reshape(new_shape)`: returns a view (if possible) with the new shape.

  ```python
  a = np.arange(6)          # [0,1,2,3,4,5]
  b = a.reshape((2, 3))     
  # [[0 1 2]
  #  [3 4 5]]
  ```
* You can use `-1` in one dimension to infer size:

  ```python
  a = np.arange(12)
  b = a.reshape((3, -1))    # shape becomes (3, 4)
  ```
* `ravel()` or `flatten()`: returns a flattened (1D) view/copy.

  ```python
  flat = b.ravel()          # view if possible
  flat2 = b.flatten()       # always returns a copy
  ```
* `resize(new_shape)`: modifies array in-place (only if array owns its data and size matches or can be changed).
* `np.resize(arr, new_shape)`: returns a new array, repeating elements if needed.

### Transpose and Axes Manipulation

* `arr.T`: transpose (swap axes for 2D; reverse axes for ND).

  ```python
  mat = np.array([[1,2,3],[4,5,6]])
  print(mat.T)
  # [[1 4]
  #  [2 5]
  #  [3 6]]
  ```
* `np.transpose(arr, axes=(...))`: specify axes order.

  ```python
  arr3 = np.arange(8).reshape((2,2,2))
  # arr3.shape = (2,2,2); transpose can reorder axes
  arr3_t = np.transpose(arr3, axes=(1,0,2))
  ```
* `np.swapaxes(arr, axis1, axis2)`: swap two axes.

---

## Stacking and Splitting Arrays

### Concatenation / Stacking

* `np.concatenate((arr1, arr2, ...), axis=?)`: join arrays along existing axis.

  ```python
  a = np.array([1,2,3])
  b = np.array([4,5,6])
  c = np.concatenate((a, b))       # [1 2 3 4 5 6]
  ```
* For 2D or higher, specify `axis`:

  ```python
  A = np.array([[1,2],[3,4]])
  B = np.array([[5,6],[7,8]])
  # Stack vertically (axis=0):
  v = np.concatenate((A, B), axis=0)
  # [[1 2]
  #  [3 4]
  #  [5 6]
  #  [7 8]]
  # Stack horizontally (axis=1):
  h = np.concatenate((A, B), axis=1)
  # [[1 2 5 6]
  #  [3 4 7 8]]
  ```
* `np.stack((arr1,arr2,...), axis=?)`: creates a new axis.

  ```python
  x = np.array([1,2,3])
  y = np.array([4,5,6])
  s0 = np.stack((x,y), axis=0)  # shape (2,3)
  s1 = np.stack((x,y), axis=1)  # shape (3,2)
  ```
* `np.hstack`, `np.vstack`, `np.dstack` are convenience functions.

### Splitting

* `np.split(arr, indices_or_sections, axis=?)`: split array into multiple sub-arrays.

  ```python
  a = np.arange(10)
  parts = np.split(a, [3, 7])  # splits at indices 3 and 7 -> [a[:3], a[3:7], a[7:]]
  ```
* `np.hsplit`, `np.vsplit`, `np.dsplit` for convenience on higher-dim arrays.

---

## Mathematical and Statistical Functions

### Basic Math

* Arithmetic: covered under elementwise operations.
* Exponentials, logs, trigonometry: see ufuncs.
* More specialized: `np.sign`, `np.abs`, `np.sqrt`, `np.power`, `np.mod`, etc.

### Statistics

* Mean, median, variance, standard deviation:

  ```python
  data = np.random.randn(1000)
  mean = np.mean(data)
  median = np.median(data)
  var = np.var(data)
  std = np.std(data)
  ```
* Percentiles:

  ```python
  p25 = np.percentile(data, 25)
  p75 = np.percentile(data, 75)
  ```
* Histogram:

  ```python
  hist, bin_edges = np.histogram(data, bins=10)
  ```
* Covariance and correlation:

  ```python
  x = np.random.randn(100)
  y = 2*x + np.random.randn(100)*0.5
  cov = np.cov(x, y)     # covariance matrix
  corr = np.corrcoef(x, y) # correlation matrix
  ```

### Linear Algebra

* Many routines in `np.linalg`:

  ```python
  A = np.array([[1, 2], [3, 4]])
  # Determinant
  detA = np.linalg.det(A)
  # Inverse
  invA = np.linalg.inv(A)
  # Eigenvalues, eigenvectors
  vals, vecs = np.linalg.eig(A)
  # Singular Value Decomposition
  U, S, Vt = np.linalg.svd(A)
  # Solve linear systems: A x = b
  b = np.array([5, 11])
  x = np.linalg.solve(A, b)
  ```
* Matrix multiplication: `@` operator or `np.dot`, `np.matmul`:

  ```python
  A = np.array([[1,2],[3,4]])
  B = np.array([[5,6],[7,8]])
  C = A @ B     # matrix product
  ```
* Note: for high-performance linear algebra, consider linking NumPy to optimized BLAS/LAPACK.

### Random Number Generation

* Use the newer `np.random.default_rng()` API (Generator) instead of legacy functions.

  ```python
  rng = np.random.default_rng()
  # Random integers
  ints = rng.integers(low=0, high=10, size=5)
  # Random floats [0,1)
  floats = rng.random(5)
  # Normal distribution
  normals = rng.normal(loc=0.0, scale=1.0, size=(2,3))
  # Choice
  choices = rng.choice([10,20,30], size=4, replace=True, p=[0.2,0.5,0.3])
  ```
* The new API provides better reproducibility and thread safety.

---

## Input/Output

### Saving and Loading `.npy` / `.npz`

* Save a single array:

  ```python
  arr = np.arange(10)
  np.save('my_array.npy', arr)
  # Load it later:
  loaded = np.load('my_array.npy')
  ```
* Save multiple arrays into a compressed `.npz`:

  ```python
  a = np.arange(5)
  b = np.arange(5, 10)
  np.savez('arrays.npz', first=a, second=b)
  # Load:
  data = np.load('arrays.npz')
  a2 = data['first']
  b2 = data['second']
  ```
* Save/load with compression:

  ```python
  np.savez_compressed('arrays_compressed.npz', first=a, second=b)
  ```

### Text Files (CSV, TXT)

* `np.savetxt` and `np.loadtxt` for simple text data:

  ```python
  data = np.random.rand(5, 3)
  np.savetxt('data.txt', data, delimiter=',', header='col1, col2, col3')
  loaded = np.loadtxt('data.txt', delimiter=',', skiprows=1)
  ```
* For more complex CSV (mixed types, missing values), consider using Pandas for convenience.

---

## Structured and Record Arrays

NumPy supports arrays with heterogeneous data types (like columns of different types).

```python
dtype = [('name', 'U10'), ('age', 'i4'), ('weight', 'f4')]
data = np.array([('Alice', 25, 55.0), ('Bob', 30, 85.5)], dtype=dtype)
# Access fields:
names = data['name']    # array(['Alice', 'Bob'], dtype='<U10')
ages = data['age']      # array([25, 30], dtype=int32)
```

* Useful for simple table-like data without needing Pandas.
* You can also create structured arrays with record arrays for attribute access:

  ```python
  rec = data.view(np.recarray)
  print(rec.name)  # ['Alice' 'Bob']
  ```

---

## Performance Tips and Best Practices

* **Prefer vectorized operations over Python loops.** E.g., use `np.sum`, array arithmetic, broadcasting, etc.
* **Minimize creating unnecessary copies.** Be aware when operations return views vs. copies.
* **Use in-place operations when possible** (e.g., `arr += 1` instead of `arr = arr + 1`) to reduce memory overhead.
* **Choose appropriate data types.** For large arrays, consider using smaller types (`float32` vs `float64`, `int32` vs `int64`) if sufficient.
* **Link against optimized BLAS/LAPACK libraries** (e.g., OpenBLAS, MKL) for better linear algebra performance.
* **Profile hotspots**: use line profilers or time small code blocks to find bottlenecks.
* **Use memory mapping** (`np.memmap`) for very large arrays that don’t fit into RAM.
* **Be careful with broadcasting**: large broadcasts may allocate big temporary arrays; check shapes.
* **Use `np.einsum`** for complex tensor operations: can be both expressive and efficient.
* **Random number generation**: use the new Generator API for reproducibility.
* When integrating with C/C++: use the buffer interface or Cython for custom performance-critical code.

---

## Interoperability with Other Libraries

* **Pandas**: DataFrame columns are often NumPy arrays under the hood. You can convert:

  ```python
  import pandas as pd
  df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
  arr = df.values        # NumPy array
  df2 = pd.DataFrame(arr, columns=['a','b'])
  ```
* **SciPy**: builds on NumPy; many scientific routines accept NumPy arrays.
* **Matplotlib**: plotting functions expect NumPy arrays.
* **TensorFlow/PyTorch**: can convert between tensors and NumPy arrays (with `.numpy()` or `torch.from_numpy`), though be careful about device (CPU/GPU).
* **scikit-learn**: expects NumPy arrays for inputs.
* **HDF5 (h5py)**: can read/write datasets as NumPy arrays.
* **Memoryviews**: when interfacing with C code, NumPy’s buffer protocol can be used.

---

## Common Pitfalls and FAQs

1. **Mutating a view affects the original**

   ```python
   a = np.arange(10)
   slice_a = a[2:5]      # view
   slice_a[0] = 100
   print(a)              # a[2] becomes 100
   ```

   * If you need a copy: use `slice_a.copy()`.

2. **Shape mismatches and broadcasting errors**

   * If shapes are incompatible for broadcasting, you’ll get a `ValueError`. Always check `arr1.shape` vs `arr2.shape`.

3. **Comparisons with floating points**

   * Avoid checking equality directly due to precision. Use `np.isclose`:

     ```python
     np.isclose(a, b)
     ```

4. **Memory usage**

   * Large arrays can consume a lot of RAM. Check `arr.nbytes`. Use appropriate dtype.

5. **Chained indexing**

   * Unlike Pandas, NumPy does not have chained indexing subtle pitfalls in the same way, but beware of mixing boolean indexing and slicing if unclear about views vs copies.

6. **Using Python loops**

   * Looping in Python over array elements is much slower than vectorized operations. Aim to express computations in array form.

7. **Random seed reproducibility**

   * Use the Generator API and seed it:

     ```python
     rng = np.random.default_rng(seed=42)
     ```

8. **Data type conversions**

   * Converting large arrays from one dtype to another can be costly. Plan ahead.

9. **Using deprecated functions**

   * Some older NumPy functions (e.g., `np.matrix`) are discouraged. Prefer arrays.

10. **Threading and parallelism**

    * NumPy operations relying on BLAS may use multiple threads. For fine-grained parallelism, consider other approaches (e.g., Numba, multiprocessing).

---

## Further Resources

* Official NumPy Documentation:
  [https://numpy.org/doc/](https://numpy.org/doc/)
* NumPy User Guide:
  [https://numpy.org/doc/stable/user/](https://numpy.org/doc/stable/user/)
* Tutorials and Guides:

  * “NumPy Quickstart Tutorial” in the official docs.
  * Various online tutorials (e.g., SciPy lectures).
* Books:

  * “Python for Data Analysis” by Wes McKinney (covers NumPy extensively).
  * “Scientific Computing with Python” resources.

---

### Example: A Mini Project Workflow

Below is a small illustrative example showing how you might use NumPy in a mini workflow: generating synthetic data, computing statistics, and saving results.

```python
import numpy as np

# 1. Generate synthetic dataset: 1000 samples, 3 features
rng = np.random.default_rng(seed=0)
data = rng.normal(loc=0.0, scale=1.0, size=(1000, 3))

# 2. Compute basic statistics column-wise
means = data.mean(axis=0)
stds = data.std(axis=0)
mins = data.min(axis=0)
maxs = data.max(axis=0)

print("Means:", means)
print("Stds:", stds)
print("Min:", mins)
print("Max:", maxs)

# 3. Normalize data (zero mean, unit variance)
data_norm = (data - means) / stds

# 4. Perform a linear transformation: rotate points in 3D
theta = np.pi / 6  # 30 degrees
# Example: rotation matrix around z-axis
rot_z = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0,              0,             1],
])
data_rotated = data_norm @ rot_z.T   # shape (1000,3)

# 5. Save normalized and rotated data
np.savez_compressed('processed_data.npz', normalized=data_norm, rotated=data_rotated)

# 6. Later, load and verify
loaded = np.load('processed_data.npz')
data_norm_loaded = loaded['normalized']
data_rot_loaded = loaded['rotated']
assert np.allclose(data_rotated, data_rot_loaded)
```

---

> **Usage Tips**:
>
> * Copy/paste code blocks into your Python REPL or scripts to experiment.
> * Use interactive environments (e.g., Jupyter notebooks) to try small snippets and inspect arrays.
> * Refer to the official documentation for deeper dives and edge cases.

---
