# Sea Level Predictor

A Python data analysis and visualization project completed as part of the **freeCodeCamp Data Analysis with Python** certification.

---

## Project Overview

This project analyzes a dataset of the **global average sea level change since 1880** and uses linear regression to predict the sea level change through the year **2050**.

Two lines of best fit are plotted — one using all data since 1880 and another using only data from 2000 onwards to reflect the more recent rate of sea level rise.

---

## Getting Started

### 1. Download the Dataset

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv" -OutFile "epa-sea-level.csv"
```

### 2. Download the Test Module

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/test_module.py" -OutFile "test_module.py"
```

### 3. Install Dependencies

```powershell
& "C:\Program Files\Python314\python.exe" -m pip install scipy
```

### 4. Run the Project

```powershell
& "C:\Program Files\Python314\python.exe" main.py
```

---

## Dataset Description

**File:** `epa-sea-level.csv`

| Column | Description |
|---|---|
| `Year` | Year of the recorded sea level measurement |
| `CSIRO Adjusted Sea Level` | Global average sea level change in inches |

**Date range:** 1880 — 2013

---

## What I Did

### Data Analysis (`sea_level_predictor.py`)

1. **Imported** the data from `epa-sea-level.csv` using pandas.
2. **Created a scatter plot** using `matplotlib` with `Year` on the x-axis and `CSIRO Adjusted Sea Level` on the y-axis.

### Line of Best Fit (All Data)

3. Used `linregress` from `scipy.stats` to calculate the slope and y-intercept using all data from 1880.
4. Extended the line through **year 2050** to predict the sea level rise.

### Line of Best Fit (2000 onwards)

5. Filtered the dataset to only include data from **year 2000** onwards.
6. Used `linregress` again to calculate a new slope and y-intercept.
7. Extended this line through **year 2050** to predict the sea level rise at the current rate.

### Chart Details

- X label: `Year`
- Y label: `Sea Level (inches)`
- Title: `Rise in Sea Level`
- Saved as `sea_level_plot.png`

---

## Generated Output

| File | Description |
|---|---|
| `output/sea_level_plot.png` | Scatter plot with two best fit lines extending to 2050 |

---

## Test Results

```
Ran 4 tests in 0.798s

OK
```

All 4 unit tests passed successfully.

---

## Tools & Libraries

- **Python** 3.14
- **pandas** 3.0.3
- **matplotlib** 3.10.9
- **scipy**

---

## References

- [freeCodeCamp – Sea Level Predictor Project](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor)
- [freeCodeCamp Boilerplate Repository](https://github.com/freeCodeCamp/boilerplate-sea-level-predictor)