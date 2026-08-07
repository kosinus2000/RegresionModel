from sklearn.base import BaseEstimator, TransformerMixin

class FeatureAdder(BaseEstimator, TransformerMixin):

    COLS_TO_DROP = [
        'GarageYrBlt',
        'Id'
    ]

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        mask = ((X['YearRemodAdd'] == 1950) & (X['YearBuilt'] < 1950))
        X.loc[mask, 'YearRemodAdd'] = X.loc[mask, 'YearBuilt']

        # total area of the house
        X['TotalSF'] = X['TotalBsmtSF'] + X['1stFlrSF'] + X['2ndFlrSF']

        # house age
        X['HouseAge'] = X['YrSold'] - X['YearBuilt']
        X['RemodelAge'] = X['YrSold'] - X['YearRemodAdd']
        X['WasRemodeled'] = (X['YearBuilt'] != X['YearRemodAdd']).astype(int)

        #bathrooms
        X['TotalBath'] = (X['FullBath'] + X['HalfBath'] * 0.5 + X['BsmtFullBath'] + X['BsmtHalfBath'] * 0.5)

        #additional features
        X['GarageAreaPerCar'] = X['GarageArea'] / (X['GarageCars'] + 1)
        X['HasPool'] = (X['PoolArea'] > 0).astype(int)
        X['HasBasement'] = (X['TotalBsmtSF'] > 0).astype(int)
        X['HasGarage'] = (X['GarageArea'] > 0).astype(int)
        X['HasFireplace'] = (X['Fireplaces'] > 0).astype(int)

        # quality of the house
        X['QualXSF'] = X['OverallQual'] * X['GrLivArea']

        return X.drop(columns=self.COLS_TO_DROP, errors='ignore')