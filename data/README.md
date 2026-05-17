# Data

## Source

Dataset from the Kaggle competition:

**House Prices: Advanced Regression Techniques**
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

## Files

| File | Description |
|---|---|
| `train.csv` | Training data (1460 records, 81 columns) |
| `test.csv` | Test data without `SalePrice` column |
| `data_description.txt` | Description of all columns |
| `sample_submission.csv` | Sample Kaggle submission file |

## Dataset Overview

- **Records:** 1460 (train) / 1459 (test)
- **Features:** 80 (+ 1 target variable)
- **Target variable:** `SalePrice` — house sale price in USD
## Column Types

| Type | Count | Examples |
|---|---|---|
| Numerical | 38 | `LotArea`, `YearBuilt`, `GrLivArea` |
| Categorical | 43 | `Neighborhood`, `HouseStyle`, `GarageType` |

## Key Features

- `GrLivArea` — above grade living area (square feet)
- `YearBuilt` — year the house was built
- `OverallQual` — overall material and finish quality (1–10)
- `Neighborhood` — neighborhood in Ames, Iowa
- `TotalBsmtSF` — total basement area (square feet)
- `GarageCars` — garage capacity (number of cars)
## Notes

- Data contains missing values — preprocessing required before training