# House Prices — Linear Regression Model

Predicting house sale prices using linear regression on the Ames Housing dataset.
Built as a learning project following the structure from *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow* by Aurélien Géron.

---

## Overview

| | |
|---|---|
| **Dataset** | [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) |
| **Records** | 1460 houses |
| **Features** | 80 (numerical + categorical) |
| **Target** | `SalePrice` — house sale price in USD |
| **Model** | Linear Regression (scikit-learn) |

---

## Project Structure

```
RegresionModel/
├── data/                   # datasets (not included in repo — see data/README.md)
│   └── README.md
├── notebooks/
│   ├── data_analize.ipynb      # exploratory data analysis
│   └── data_edition.ipynb      # data cleaning and feature engineering
├── src/
│   ├── data_loader.py      # loading and splitting data
│   ├── preprocessing.py    # feature engineering and transformations
│   └── evaluate.py         # metrics (RMSE, R²)
├── models/
│   └── linear_regression.pkl
├── requirements.txt
└── README.md
```

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/RegresionModel.git
cd RegresionModel
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download the dataset**

Download `train.csv` from [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) and place it in the `data/` folder.

**4. Run**
```bash
python src/data_loader.py
```

---

## Results

| Metric | Value |
|---|---|
| RMSE | — |
| R² | — |

*Results will be updated after model training.*

---

## Tech Stack

- Python 3.x
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn

---

## References

- Géron, A. — *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*
- [Kaggle — House Prices Competition](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)