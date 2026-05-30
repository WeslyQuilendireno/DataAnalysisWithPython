# Demographic Data Analyzer

A Python data analysis project completed as part of the **freeCodeCamp Data Analysis with Python** certification.

---

## Project Overview

This project analyzes demographic data extracted from the **1994 Census database** using `pandas`. The dataset contains information about age, education, occupation, race, sex, working hours, and salary of individuals.

The goal is to answer specific demographic questions by performing data analysis and aggregation using pandas.

---

## Getting Started

### 1. Download the Dataset

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/main/adult.data.csv" -OutFile "adult.data.csv"
```

### 2. Download the Test Module

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/main/test_module.py" -OutFile "test_module.py"
```

### 3. Run the Project

```powershell
& "C:\Program Files\Python314\python.exe" main.py
```

---

## Dataset Description

**File:** `adult.data.csv`

| Column | Description |
|---|---|
| `age` | Age of the individual |
| `workclass` | Type of employment |
| `fnlwgt` | Final weight |
| `education` | Highest education level |
| `education-num` | Number of years of education |
| `marital-status` | Marital status |
| `occupation` | Type of occupation |
| `relationship` | Relationship status |
| `race` | Race of the individual |
| `sex` | Sex of the individual |
| `capital-gain` | Capital gains |
| `capital-loss` | Capital losses |
| `hours-per-week` | Hours worked per week |
| `native-country` | Country of origin |
| `salary` | Salary category (`<=50K` or `>50K`) |

---

## What I Did

### Questions Answered (`demographic_data_analyzer.py`)

1. **Race count** — Number of people of each race represented in the dataset using `value_counts()`.
2. **Average age of men** — Mean age of all male individuals, rounded to 1 decimal.
3. **Percentage with Bachelor's degree** — Percentage of people whose education is `Bachelors`.
4. **Higher education earning >50K** — Percentage of people with `Bachelors`, `Masters`, or `Doctorate` who earn `>50K`.
5. **Lower education earning >50K** — Percentage of people without advanced education who earn `>50K`.
6. **Minimum hours worked** — Minimum number of hours worked per week in the dataset.
7. **Rich percentage among minimum hour workers** — Percentage of people working the minimum hours who earn `>50K`.
8. **Highest earning country** — Country with the highest percentage of people earning `>50K` and what that percentage is.
9. **Top occupation in India** — Most popular occupation among people from India who earn `>50K`.

### Results

| Question | Answer |
|---|---|
| Average age of men | 39.4 |
| Percentage with Bachelor's degree | 16.4% |
| Higher education earning >50K | 46.5% |
| Lower education earning >50K | 17.4% |
| Minimum hours worked | 1 hour/week |
| Rich % among min hour workers | 10.0% |
| Country with highest % earning >50K | Iran |
| Highest % earning >50K | 41.9% |
| Top occupation in India (>50K) | Prof-specialty |

---

## Test Results

```
Ran 10 tests in 0.103s

OK
```

All 10 unit tests passed successfully.

---

## Tools & Libraries

- **Python** 3.14
- **pandas** 3.0.3

---

## References

- [freeCodeCamp – Demographic Data Analyzer Project](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer)
- [freeCodeCamp Boilerplate Repository](https://github.com/freeCodeCamp/boilerplate-demographic-data-analyzer)