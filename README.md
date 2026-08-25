# Ames House Price Prediction

A machine-learning project for predicting residential property sale prices using the **House Prices: Advanced Regression Techniques** dataset. The project covers exploratory data analysis, feature engineering, model comparison, hyperparameter tuning, and Kaggle-ready prediction generation.

## Dataset

The data comes from Kaggle's [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) competition.

| File | Rows | Description |
| --- | ---: | --- |
| `train.csv` | 1,460 | 80 property features and the target variable, `SalePrice` |
| `test.csv` | 1,459 | Property features without `SalePrice` |

The dataset files are not tracked in the repository. Download them from the Kaggle competition and place them in `data/`. See [`data/data_description.txt`](data/data_description.txt) for the original feature reference.

## Project Structure

```text
RegresionModel/
├── data/
│   ├── train.csv                         # training data; downloaded separately
│   ├── test.csv                          # prediction data; downloaded separately
│   ├── sample_submission.csv             # Kaggle submission example
│   └── data_description.txt              # feature descriptions
├── models/
│   └── final_model.pkl                   # trained scikit-learn pipeline
├── notebooks/
│   ├── 01_data_analize.ipynb             # exploratory data analysis
│   ├── 02_data_edition.ipynb             # data preparation and feature engineering
│   └── 03_model.ipynb                    # model evaluation, tuning, and export
├── reports/
│   └── housing_output.csv                # generated predictions
├── src/
│   ├── data_loader.py                    # training-data loader
│   └── transformers.py                   # custom FeatureAdder transformer
├── main.py                               # prediction script
└── requirements.txt
```

## Setup

Requirements: Python 3 and `pip`.

```bash
git clone <repository-url>
cd RegresionModel
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Download `train.csv` and `test.csv` from the [competition data page](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data), then put both files in `data/`.

## Generate Predictions

The repository includes a trained model. From the project root, run:

```bash
python main.py
```

The script loads `models/final_model.pkl`, predicts prices for `data/test.csv`, and writes `reports/housing_output.csv`. The generated file contains the `Id` and `SalePrice` columns required for a Kaggle submission.

## Modelling Workflow

The notebooks document the full workflow:

1. `01_data_analize.ipynb` explores the Ames Housing data.
2. `02_data_edition.ipynb` prepares the data and develops features.
3. `03_model.ipynb` evaluates linear regression, decision tree, random forest, Ridge regression, and neural-network approaches; it also tunes candidate models with cross-validation.

The exported final pipeline uses a tuned `RandomForestRegressor` with preprocessing for numerical and categorical features. Its recorded hold-out test-set RMSE is **30,428.73 USD**.

## Feature Engineering

The custom [`FeatureAdder`](src/transformers.py) creates and adjusts features including:

- total floor area (`TotalSF`);
- property age, remodel age, and remodel flag;
- total bathroom count (`TotalBath`);
- garage area per car;
- binary indicators for a pool, basement, garage, and fireplace;
- an interaction between overall quality and living area (`QualXSF`).

## Technology Stack

- Python
- scikit-learn
- pandas and NumPy
- matplotlib and seaborn
- Jupyter
- joblib

## References

- Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*
- [Kaggle — House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
