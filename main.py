import joblib
import pandas as pd

from src.transformers import FeatureAdder

MODEL_PATH = 'models/final_model.pkl'
DATA_PATH = 'data/test.csv'
OUTPUT_PATH = 'reports/housing_output.csv'

def main():

    model = joblib.load(MODEL_PATH)
    data = pd.read_csv(DATA_PATH)
    print(f'Załadowane dane z pliku: {DATA_PATH}')

    prediction = model.predict(data)

    results = pd.DataFrame({
        'Id': data['Id'],
        'SalePrice': prediction,
    })

    results.to_csv(OUTPUT_PATH, index=False)


if __name__ == '__main__':
    main()