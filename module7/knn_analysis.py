"""KNN Analysis of Movies
"""
import pandas as pd
import numpy as np
import get_data as gt # your package

# Constants
K = 10 # number of closest matches
BASE_CASE_ID = 88763 # IMDB_id for 'Back to the Future'


def knn_analysis_driver(df, base_case, comparison_type, metric_stub, sorted_value='metric'):
    # WIP: Create df of filter data
    df[sorted_value] = df[comparison_type].map(lambda x: metric_stub(base_case[comparison_type], x))


def main():
    # TASK 1: Get dataset from server
    print(f'Task 1: Download dataset from server')
    dataset_file = 'movies.csv'
    gt.download_dataset(gt.ICARUS_CS4580_DATASET_URL, dataset_file)
    # TASK 2: Load  data_file into a DataFrame
    print(f'Task 2: Load movie data into a DataFrame')
    data_file = f'{gt.DATA_FOLDER}/{dataset_file}'
    data = gt.load_data(data_file, index_col='IMDB_id')
    print(f'Loaded {len(data)} records')
    print(f'Data set Columns {data.columns}')
    print(f'Data set description {data.describe()}')
    # TODO: The rest of your code goes here



if __name__ == '__main__':
    main()
