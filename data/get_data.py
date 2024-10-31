"""Download data from our server
"""
import requests
import shutil
import os


SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Download data from a URL and save it to a local file.
When needed, the file will be extracted from compressed format.
"""
# import pandas as pd
# import numpy as np
import requests
import shutil
import os, sys
import zipfile

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data'


def extract_zip_file(zip_path):
    """Extract a ZIP file to the current working directory.

    Args:
        zip_path (str): Zip file absolute path
    """
    
    print(f"Extracting {zip_path}")
    # Get the current working directory
    extract_path = os.getcwd()
    
    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents to the current working directory
        zip_ref.extractall(extract_path)
        print(f"File unzipped successfully and extracted to {extract_path}")
        # List the extracted files
        print(f"Extracted files: {zip_ref.namelist()}")
    # Delete the zip file
    os.remove(zip_path)


#TODO: Create a function to download the files
# from Kaggle directly by passing the dataset name

def download_zip_file(url):
    """Download a ZIP file from a URL and save it to a local file.

    Args:
        url (url): File URL to download
    """
    # Get the current working directory
    dest_path = os.path.join(os.getcwd(), os.path.basename(url))
    
    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open the destination file in write-binary mode
        with open(dest_path, 'wb') as out_file:
            # Copy the response content to the destination file
            shutil.copyfileobj(response.raw, out_file)
        print(f"File downloaded successfully and saved to {dest_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

    # Check file extension. If it is a ZIP file, extract it
    if dest_path.endswith('.zip'):
        extract_zip_file(dest_path)


def main():
    """
    TBD: Method DocString
    """

    
    # TODO: Enable options for downloading sources
    # -i for icarus server <FILE>
    # -k for kaggle <DATASET>
    # -s for other server: <SERVER> <FILE>
    # If no arguments are provided, print a usage message
    if len(sys.argv) < 2:
        print("Usage: python download_data.py <data_file>")
        sys.exit(1)

    #data01 = f'{SERVER_URL}/pandas01Data.zip'
    # Take data file as input parameter
    data_file = sys.argv[1]
    print(f"Data file: {data_file}")
    data01 = f'{SERVER_URL}/{data_file}'
    download_zip_file(data01)
    # TODO: Set input user options to extract files
    # from different sources: -url, -kaggle



if __name__ == '__main__':
    main()