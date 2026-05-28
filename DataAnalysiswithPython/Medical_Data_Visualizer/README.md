# Medical Data Visualizer

A Python data analysis and visualization project completed as part of the **freeCodeCamp Data Analysis with Python** certification.

---

## Project Overview

This project visualizes and makes calculations from medical examination data using `matplotlib`, `seaborn`, and `pandas`. The dataset was collected during medical examinations and contains information about patients' body measurements, blood test results, and lifestyle choices.

The goal is to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

---

## Getting Started

### 1. Download the Dataset

The dataset `medical_examination.csv` was downloaded from the official freeCodeCamp boilerplate repository using the following command:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv" -OutFile "medical_examination.csv"
```

### 2. Install Dependencies

```powershell
& "C:\Program Files\Python314\python.exe" -m pip install numpy
& "C:\Program Files\Python314\python.exe" -m pip install pandas
& "C:\Program Files\Python314\python.exe" -m pip install seaborn
& "C:\Program Files\Python314\python.exe" -m pip install matplotlib
```

### 3. Run the Project

```powershell
& "C:\Program Files\Python314\python.exe" main.py
```

---

## Dataset Description

**File:** `medical_examination.csv`

| Feature | Variable Type | Variable | Value Type |
|---|---|---|---|
| Age | Objective | `age` | int (days) |
| Height | Objective | `height` | int (cm) |
| Weight | Objective | `weight` | float (kg) |
| Gender | Objective | `gender` | categorical code |
| Systolic blood pressure | Examination | `ap_hi` | int |
| Diastolic blood pressure | Examination | `ap_lo` | int |
| Cholesterol | Examination | `cholesterol` | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination | `gluc` | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective | `smoke` | binary |
| Alcohol intake | Subjective | `alco` | binary |
| Physical activity | Subjective | `active` | binary |
| Cardiovascular disease | Target | `cardio` | binary |

---

## What I Did

### Data Preparation (`medical_data_visualizer.py`)

1. **Imported** the data from `medical_examination.csv` into a pandas DataFrame.
2. **Added an `overweight` column** by calculating BMI (`weight / (height/100)²`). Values above 25 are marked as `1` (overweight), otherwise `0`.
3. **Normalized** `cholesterol` and `gluc` columns — values of `1` become `0` (good), values above `1` become `1` (bad).

### Categorical Plot (`draw_cat_plot`)

4. Used `pd.melt` to reshape the DataFrame with `cardio` as the ID variable.
5. Grouped and counted the data by `cardio`, `variable`, and `value`.
6. Created a bar chart using `sns.catplot()` showing counts of `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight` split by `cardio`.
7. Saved the output as `catplot.png`.

### Heat Map (`draw_heat_map`)

8. Cleaned the data by filtering out incorrect values:
   - Diastolic pressure (`ap_lo`) must be ≤ systolic pressure (`ap_hi`)
   - Height and weight must be within the 2.5th–97.5th percentile range
9. Calculated the **correlation matrix** using `df.corr(numeric_only=True)`.
10. Generated a **mask** for the upper triangle to avoid duplication.
11. Plotted the heatmap using `sns.heatmap()` with annotations.
12. Saved the output as `heatmap.png`.

---

## Generated Output

| File | Description |
|---|---|
| `output/catplot.png` | Categorical bar chart of health variables split by cardiovascular disease |
| `output/heatmap.png` | Correlation heatmap of all medical features |

---

## Test Results

```
Ran 4 tests in 2.315s

OK
```

All 4 unit tests passed successfully.

---

## Tools & Libraries

- **Python** 3.14
- **pandas** 3.0.3
- **seaborn** 0.13.2
- **matplotlib** 3.10.9
- **numpy** 2.4.6

---

## References

- [freeCodeCamp – Medical Data Visualizer Project](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)
- [freeCodeCamp Boilerplate Repository](https://github.com/freeCodeCamp/boilerplate-medical-data-visualizer)