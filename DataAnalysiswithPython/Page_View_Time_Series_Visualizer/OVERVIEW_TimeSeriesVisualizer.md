# Time Series Visualizer

Still debugging — `test_data_cleaning` fails due to a **pandas 3.0 incompatibility in the freeCodeCamp test file**, not the project code. All 3 charts generate correctly.

---

## Project Overview

This project visualizes time series data using line charts, bar charts, and box plots with `matplotlib`, `seaborn`, and `pandas`. The dataset contains the number of daily page views on the freeCodeCamp.org forum from **2016-05-09 to 2019-12-03**.

---

## Getting Started

### 1. Download the Dataset

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/main/fcc-forum-pageviews.csv" -OutFile "fcc-forum-pageviews.csv"
```

### 2. Download the Test Module

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/main/test_module.py" -OutFile "test_module.py"
```

### 3. Run the Project

```powershell
& "C:\Program Files\Python314\python.exe" main.py
```

---

## What I Did

### Data Preparation

1. Imported `fcc-forum-pageviews.csv` using pandas with `date` as the index.
2. Cleaned the data by filtering out the top 2.5% and bottom 2.5% of page view values.

### Line Chart (`draw_line_plot`)

3. Plotted daily page views using `matplotlib`.
4. Title: `Daily freeCodeCamp Forum Page Views 5/2016-12/2019`
5. X axis: `Date`, Y axis: `Page Views`
6. Saved as `line_plot.png`.

### Bar Chart (`draw_bar_plot`)

7. Grouped data by year and month, calculated average daily page views.
8. Created a grouped bar chart showing average monthly page views per year.
9. X axis: `Years`, Y axis: `Average Page Views`, Legend: `Months`
10. Saved as `bar_plot.png`.

### Box Plots (`draw_box_plot`)

11. Created two adjacent box plots using `seaborn`:
    - **Year-wise Box Plot (Trend)** — distribution of page views per year
    - **Month-wise Box Plot (Seasonality)** — distribution per month (Jan–Dec)
12. Saved as `box_plot.png`.

---

## Generated Output

| File | Description |
|---|---|
| `output/line_plot.png` | Daily page views from 2016 to 2019 |
| `output/bar_plot.png` | Average monthly page views grouped by year |
| `output/box_plot.png` | Year-wise and month-wise distribution box plots |

---

## Test Results

```
Ran 11 tests in 6.409s

FAILED (errors=1)
```

> ⚠️ The 1 failure (`test_data_cleaning`) is caused by a **pandas 3.0 incompatibility in the freeCodeCamp test file**. The test calls `int(df.count(numeric_only=True))` which returns a `Series` in pandas 3.0 instead of a scalar. All 3 charts generate correctly and all other 10 tests pass.

---

## Tools & Libraries

- **Python** 3.14
- **pandas** 3.0.3
- **seaborn** 0.13.2
- **matplotlib** 3.10.9
- **numpy** 2.4.6

---

## References

- [freeCodeCamp – Page View Time Series Visualizer Project](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer)
- [freeCodeCamp Boilerplate Repository](https://github.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer)