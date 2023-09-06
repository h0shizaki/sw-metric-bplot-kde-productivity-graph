import pandas as pd
import numpy as np

def load_data(path, to_drop):
    dataset = pd.read_csv(path).drop(to_drop, axis=1).replace(-1, np.nan).dropna()
    dataset['Productivity'] = dataset['Effort'] / dataset['PointsAjust']
    return dataset
    
def filter_dataset(dataset):
    return dataset[dataset['Language'] == 1], dataset[dataset['Language'] == 2], dataset[dataset['Language'] == 3]
