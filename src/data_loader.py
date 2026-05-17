import zipfile

import pandas as pd
from pathlib import Path

def data_loader():
    """Loads the housing dataset."""
    csv_path = Path(__file__).parent.parent / "data" / "train.csv"
    zip_path = Path(__file__).parent.parent / "data" / "house-prices-advanced-regression-techniques.zip"

    if not csv_path.exists():
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(Path(__file__).parent.parent / "data")

    return pd.read_csv(csv_path)

housing = data_loader()