#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
CS 4580 - Assignment 5. Titanic Crew Analysis
"""
import sys, os
import requests
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# import matplotlib.pyplot as plt

# Constants
ICARUS_CS4580_DATASET_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data'
DATA_FOLDER = 'data'
    

def download_dataset(url, data_file, data_folder=DATA_FOLDER):
    """
    Downloads a dataset from a specified URL and saves it to a local directory.
    Parameters:
    url (str): The base URL where the dataset is hosted.
    data_file (str): The name of the dataset file to be downloaded.
    data_folder (str): The name of the data folder to store data
    Returns:
    None
    Side Effects:
    - Creates a directory if it does not exist.
    - Downloads the dataset file and saves it to the specified directory.
    - Prints messages indicating the status of the download process.
    Notes:
    - If the dataset file already exists in the specified directory, the function will not download it again.
    - If the download fails, an error message will be printed.
    """
    
    # Check if the data folder exists and file_path is a valid path
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        print(f'Created folder {data_folder}')
    # Check if the file already exists
    data_folder = os.path.join(data_folder, data_file)
    if os.path.exists(data_folder):
        print(f'Dataset {data_file} already exists in {data_folder}')
        return

    # Include file name to url server address
    url = f'{url}/{data_file}'
    # Download the dataset from the server to DATA_FOLDER
    response = requests.get(url)
    if response.status_code == 200:
        with open(data_folder, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded dataset {data_file} to {data_folder}')
    else:
        print(f'Error downloading dataset {data_file} from {url}')
    


def load_data(file_path, index_col=None):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.
    index_col (str): Optional column for DataFrame index

    Returns:
    DataFrame: Returns a pandas DataFrame if the file exists and is a valid CSV file.

    Raises:
    ValueError: If the file is not a valid CSV file.
    FileNotFoundError: If the file does not exist.
    """
    # Check if file is csv format
    if not file_path.endswith('.csv'):
        print(f'File {file_path} is not a valid CSV file')
        raise ValueError
    # Check if data is a valid file path or raise an error
    if not os.path.exists(file_path):
        print(f'File {file_path} does not exist')
        raise FileNotFoundError

    # Load the data into a DataFrame
    if index_col:
        df = pd.read_csv(file_path, index_col=index_col)
    else:
        df = pd.read_csv(file_path)

    return df



def main():
    # TASK 1: Get dataset from server
    print(f'Task 1: Download dataset from server')
    dataset_file = 'movies.csv'
    download_dataset(ICARUS_CS4580_DATASET_URL, dataset_file)
    # TASK 2: Load  data_file into a DataFrame
    print(f'Task 2: Load weather data into a DataFrame')
    data_file = f'{DATA_FOLDER}/{dataset_file}'
    data = load_data(data_file, index_col='IMDB_id')
    print(f'Loaded {len(data)} records')
    # TODO: The rest of your code goes here



if __name__ == '__main__':
    main()
