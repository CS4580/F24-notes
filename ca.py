#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
CS 4580 - Assignment 4
"""
import pandas as pd
import matplotlib.pyplot as plt
import sys, os
from sklearn.preprocessing import LabelEncoder
    

def load_data(file_path):
    """
    Loads data from a CSV file

    Args:
        file_path (str): The path to the CSV file containing the census data.

    Returns:
        pandas.DataFrame: A DataFrame containing the weather data
    """
    # TBD: Implement the function to load data
    df = pd.read_csv(file_path)
    return df


def get_start_end_date(data):
    # TODO: Implement the function to get the start and end date of the data
    pass


def get_avg_min_temp_by_month(data):
    # TODO: Implement the function to get the average minimum temperature by month
    pass


def plot_avg_min_temp_by_month(avg_min_temp):
    # TODO: Implement the function to plot the average minimum temperature by month
    pass
    

def get_unique_cities(data):
    # TODO: Implement the function to get the unique cities in the data
    pass


def print_top_rainiest_cities(data, n=5):
    # TODO: Implement the function to print the top n rainiest cities
    pass
    

def print_univariate_values(data):
    # TODO: Implement the function to print the univariate values
    # print(f'Mean Pressure9am: {data["Pressure9am"].mean():.2f}')
    pass


def fix_missing_values(data, column):
    #TODO: Implement the function to fix missing values
    pass
    

def get_correlation_two_vars(data, var1, var2, type_correlation='pearson'):
    from scipy.stats import pearsonr, spearmanr
    # TODO: Implement the function to get the correlation between two variables
    pass
    
    
def plot_correlation(data, var1, var2):
    # TODO: Implement the function to plot the correlation between two variables
    pass

def encode_categorical_data(data, column):
    # TODO: Implement the function to encode categorical data
    pass



def show_correlation_cities_rainfall(data, col1, col2, type_correlation='pearson'):
    # TODO: Implement the function to show the correlation between cities and rainfall
    pass


def main():
    # TASK 1: Get dataset from Kaggle
    # TASK 2: Load census data into a DataFrame
    print(f'Task 2: Load weather data into a DataFrame')
    census_data_file = 'data/weatherAUS.csv'
    data = load_data(census_data_file)
    print(f'Loaded {len(data)} records')

    # # TASk 3: Print (to the console) the start to end of the time in days, months, and years.
    # print(f'\nTask 3: Print the start and end of the time in days, months, and years')
    # min_date, max_date = get_start_end_date(data)
    # print(f'Start Date: {min_date}')
    # print(f'End Date: {max_date}')

    # # TASK 4: Print (to the console) the average MinTemp based on month (you should display 12 values).
    # print(f'\nTask 4: Print the average MinTemp based on month')
    # avg_min_temp = get_avg_min_temp_by_month(data)
    # print(f'Average MinTemp by Month: {avg_min_temp}')

    # # Task 5: Display this information in a bar chart (or histogram) using the 'matplotlib' or 'plotly' package. 
    # # The x-axis should be the month and the y-axis should be the average MinTemp.
    # print(f'\nTask 5: Display the average MinTemp by month in a bar chart')
    # plot_avg_min_temp_by_month(avg_min_temp)

    # # TASK 6: Get Unique Cities
    # print(f'\nTask 6: Get Unique Cities')
    # unique_cities = get_unique_cities(data)
    # print(f'Unique Cities: {unique_cities}')

    # # TASK 7: Print out the top five rainiest cities in the dataset.
    # total = 5
    # print(f'\nTask 7: Print the top five rainiest cities in the dataset')
    # rainiest_cities = print_top_rainiest_cities(data, n=total)
    # print(f'Top {total} Rainiest Cities: {rainiest_cities}')

    # # TASK 8: Print out different univariate values 
    # print(f'\nTask 8: Print univariate values')
    # print_univariate_values(data)

    # # TASK 9: Fix missing values
    # print(f'\nTask 9: Fix missing values for MinTemp and Rainfall')
    # col1 = 'MinTemp'
    # fix_missing_values(data, col1)
    # col2 = 'Rainfall'
    # fix_missing_values(data, col2)
    
    # # TASK 10: Show the correlation between MinTemp and Rainfall
    # print(f'\nTask 10: Show the correlation between MinTemp and Rainfall')
    # correlations = ['pearson', 'spearman']
    # for correlation in correlations:
    #     corr, p_value  = get_correlation_two_vars(data, col1, col2, type_correlation=correlation)
    #     # Display p_value in scientific notation up to -22
    #     print(f'{correlation.capitalize()} Correlation ({col1}, {col2}): {corr:.6f}. P-value: {p_value:.21e}')   
    #     # TASK 10B: Explain the correlation in the console
    
    # TASK 10C: Plot the correlation
    # plot_correlation(data, col1, col2)

    # # Task 11: Second correlation
    # correlation = 'pearson'
    # col1 = 'Location'
    # col2 = 'Rainfall'
    # print(f'\nTask 11: Show the correlation between {col1} and {col2}')   
    # corr, p_value = show_correlation_cities_rainfall(data, col1, col2, type_correlation=correlation)
    # print(f'{correlation.capitalize()} Correlation ({col1}, {col2}): {corr:.6f}. P-value: {p_value:.21e}')   
    

if __name__ == '__main__':
    main()
