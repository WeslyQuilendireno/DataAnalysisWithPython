# Mean-Variance-Standard Deviation Calculator

A Python data analysis project completed as part of the **freeCodeCamp Data Analysis with Python** certification.

---

## Project Overview

This project creates a function that uses **Numpy** to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a **3 x 3 matrix**.

The input is a list of 9 digits which gets converted into a 3 x 3 Numpy array, then statistical calculations are performed along both axes and on the flattened matrix.

---

## Getting Started

### 1. Run the Project

```powershell
cd C:\Users\Weshiwes\Desktop\DataAnalysiswithPython\Mean-Variance-Standard_Deviation_Calculator
& "C:\Program Files\Python314\python.exe" main.py
```

---

## What I Did

### Function (`mean_var_std.py`)

1. **Validated input** — raises `ValueError` with the message `"List must contain nine numbers."` if the input list has fewer than 9 elements.
2. **Reshaped** the input list into a 3 x 3 Numpy array using `np.array().reshape(3, 3)`.
3. **Calculated** the following statistics along `axis=0` (columns), `axis=1` (rows), and the flattened matrix:
   - Mean
   - Variance
   - Standard Deviation
   - Max
   - Min
   - Sum
4. **Returned** all results as a dictionary with lists (not Numpy arrays) using `.tolist()`.

### Expected Output Format

```python
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

### Example

Input: `calculate([0,1,2,3,4,5,6,7,8])`

Output:
```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.667, 0.667, 0.667], 6.667],
  'standard deviation': [[2.449, 2.449, 2.449], [0.816, 0.816, 0.816], 2.582],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

---

## Test Results

```
Ran 3 tests in 0.001s

OK
```

All 3 unit tests passed successfully.

---

## Tools & Libraries

- **Python** 3.14
- **numpy** 2.4.6

---

## References

- [freeCodeCamp – Mean-Variance-Standard Deviation Calculator Project](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)
- [freeCodeCamp Boilerplate Repository](https://github.com/freeCodeCamp/boilerplate-mean-variance-standard-deviation-calculator)