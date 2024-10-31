import pytest
import pandas as pd
import ca  #  UPDATE to student file name
import matplotlib.pyplot as plt
from unittest.mock import patch


# Common fixture for all tests
@pytest.fixture
def load_data():
    data_file = 'data/weatherAUS.csv'
    return ca.load_data(data_file)


def test_get_start_end_date(load_data):
    
    data = load_data # Get dataFrame from fixture
    
    # Convert the 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Call the function
    start_date, end_date = ca.get_start_end_date(data)
    
    # Assert the results
    assert start_date == pd.Timestamp('2007-11-01')
    assert end_date == pd.Timestamp('2017-06-25')

def test_get_start_end_date_empty(load_data):
    # data = load_data # Get dataFrame from fixture
    
    # Create an empty DataFrame
    data = pd.DataFrame({'Date': []})
    
    # Convert the 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Call the function
    start_date, end_date = ca.get_start_end_date(data)
    
    # Assert the results
    assert pd.isna(start_date)
    assert pd.isna(end_date)

def test_get_avg_min_temp_by_month(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Call the function
    avg_min_temp = ca.get_avg_min_temp_by_month(data)
    
    # Assert the results
    assert len(avg_min_temp) == 12  # There should be 12 months
    assert avg_min_temp.index.min() == 1  # The minimum index should be 1 (January)
    assert avg_min_temp.index.max() == 12  # The maximum index should be 12 (December)
    assert avg_min_temp.notna().all()  # Ensure there are no NaN values in the result

def test_get_avg_min_temp_by_month_value(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Call the function
    avg_min_temp = ca.get_avg_min_temp_by_month(data)

    # Assert the values for a few month, up to two decimal places
    assert avg_min_temp[1] == pytest.approx(17.53, rel=1e-2)
    assert avg_min_temp[5] == pytest.approx(9.64, rel=1e-2)
    assert avg_min_temp[10] == pytest.approx(11.53, rel=1e-2)


def test_plot_avg_min_temp_by_month(load_data):
    data = load_data  # Get dataFrame from fixture
    avg_min_temp = ca.get_avg_min_temp_by_month(data)

    with patch('matplotlib.pyplot.show') as mock_show, \
            patch('matplotlib.pyplot.savefig') as mock_savefig, \
            patch('matplotlib.pyplot.bar') as mock_bar, \
            patch('matplotlib.pyplot.xlabel') as mock_xlabel, \
            patch('matplotlib.pyplot.ylabel') as mock_ylabel, \
            patch('matplotlib.pyplot.title') as mock_title:

        ca.plot_avg_min_temp_by_month(avg_min_temp)

        # Check if the bar plot was created with the correct data
        mock_bar.assert_called_once_with(avg_min_temp.index, avg_min_temp.values)
        
        # Check if the labels and title were set correctly
        mock_xlabel.assert_called_once_with('Month')
        mock_ylabel.assert_called_once_with('Average Minimum Temperature')
        mock_title.assert_called_once_with('Average Minimum Temperature by Month')
        
        # Check if the plot was saved as a PNG file
        mock_savefig.assert_called_once_with('plots/avg_min_temp_by_month.png')
        
        # Check if the plot was shown
        mock_show.assert_called_once()

def test_get_unique_cities(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Call the function
    unique_cities = ca.get_unique_cities(data)
    
    # Assert the result
    assert unique_cities == 49  # Assuming there are 49 unique cities in the dataset

def test_get_unique_cities_empty():
    # Create an empty DataFrame
    data = pd.DataFrame({'Location': []})
    
    # Call the function
    unique_cities = ca.get_unique_cities(data)
    
    # Assert the result
    assert unique_cities == 0  # There should be 0 unique cities in an empty dataset

def test_print_top_rainiest_cities(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Call the function
    top_cities = ca.print_top_rainiest_cities(data, n=5)
    
    # Assert the result
    assert len(top_cities) == 5  # There should be 5 cities in the result
    assert isinstance(top_cities, list)  # The result should be a list
    assert all(isinstance(city, str) for city in top_cities)  # All elements should be strings

def test_print_top_rainiest_cities_value(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Call the function
    top_cities = ca.print_top_rainiest_cities(data, n=5)
    
    # Assert the values (assuming known top cities)
    expected_top_cities = ['Cairns', 'Darwin', 'CoffsHarbour', 'GoldCoast', 'Sydney']
    assert top_cities == expected_top_cities

def test_print_top_rainiest_cities_empty():
    # Create an empty DataFrame
    data = pd.DataFrame({'Location': [], 'Rainfall': []})
    
    # Call the function
    top_cities = ca.print_top_rainiest_cities(data, n=5)
    
    # Assert the result
    assert top_cities == []  # There should be no cities in the result

def test_print_top_rainiest_cities_less_than_n(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Filter data to have less than 'n' cities
    filtered_data = data[data['Location'].isin(['Sydney', 'Melbourne'])]
    
    # Call the function
    top_cities = ca.print_top_rainiest_cities(filtered_data, n=5)
    
    # Assert the result
    assert len(top_cities) == 2  # There should be 2 cities in the result
    assert set(top_cities) == {'Sydney', 'Melbourne'}  # The cities should be Sydney and Melbourne

def test_print_univariate_values(load_data, capsys):
    data = load_data  # Get dataFrame from fixture
    
    # Call the function
    ca.print_univariate_values(data)
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert the output contains expected values
    assert "Mean Pressure9am: 1017.65" in captured.out
    assert "Mode Humidity9am: 99.00" in captured.out
    assert "Median WindGustSpeed: 39.00" in captured.out
    assert "Standard Deviation Temp3pm: 6.94" in captured.out
    assert "75th Percentile Rainfall: 0.80" in captured.out
    assert "Minimum MaxTemp: -4.80" in captured.out
    assert "Maximum MinTemp: 33.90" in captured.out
    assert "Range WindSpeed9am: 130.00" in captured.out
    assert "Variance Evaporation: 17.59" in captured.out
    assert "Skewness Sunshine: -0.50" in captured.out

    # assert corr == pytest.approx(0.10, rel=1e-2)

def test_fix_missing_values(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Introduce missing values in a column
    data.loc[0, 'MinTemp'] = None
    data.loc[1, 'MinTemp'] = None
    
    # Call the function
    ca.fix_missing_values(data, 'MinTemp')
    
    # Assert the missing values are filled with the median
    median_value = data['MinTemp'].median()
    assert data.loc[0, 'MinTemp'] == median_value
    assert data.loc[1, 'MinTemp'] == median_value

def test_fix_missing_values_no_missing(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Ensure there are missing values in the column
    assert data['MinTemp'].isnull().sum() > 0
    assert data['Rainfall'].isnull().sum() > 0
    
    # Call the function
    ca.fix_missing_values(data, 'MinTemp')
    ca.fix_missing_values(data, 'Rainfall')
    
    # Assert the data remains unchanged
    assert data['MinTemp'].isnull().sum() == 0
    assert data['Rainfall'].isnull().sum() == 0

def test_fix_missing_values_empty_column():
    # Create an empty DataFrame with the specified column
    data = pd.DataFrame({'MinTemp': []})
    
    # Call the function
    ca.fix_missing_values(data, 'MinTemp')
    
    # Assert the data remains unchanged
    assert data['MinTemp'].isnull().sum() == 0


def test_fix_missing_values_nonexistent_column(load_data):
    data = load_data  # Get dataFrame from fixture

    # Call the function with a nonexistent column
    with pytest.raises(KeyError):
        ca.fix_missing_values(data, 'NonExistentColumn')

def test_get_correlation_two_vars(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Need to run fix_missing_values to fill missing values
    ca.fix_missing_values(data, 'MinTemp')
    ca.fix_missing_values(data, 'Rainfall')
    # Call the function for Pearson correlation
    corr, p_value = ca.get_correlation_two_vars(data, 'MinTemp', 'Rainfall', type_correlation='pearson')
    
    # Assert the results
    assert isinstance(corr, float)  # Correlation should be a float
    assert isinstance(p_value, float)  # p-value should be a float
    assert -1 <= corr <= 1  # Correlation coefficient should be between -1 and 1

def test_get_correlation_two_vars_spearman(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Need to run fix_missing_values to fill missing values
    ca.fix_missing_values(data, 'MinTemp')
    ca.fix_missing_values(data, 'MaxTemp')
    # Call the function for Spearman correlation
    corr, p_value = ca.get_correlation_two_vars(data, 'MinTemp', 'MaxTemp', type_correlation='spearman')
    
    # Assert the results
    assert isinstance(corr, float)  # Correlation should be a float
    assert isinstance(p_value, float)  # p-value should be a float
    assert -1 <= corr <= 1  # Correlation coefficient should be between -1 and 1

def test_get_correlation_two_vars_invalid_correlation_type(load_data):
    data = load_data  # Get dataFrame from fixture
    # Need to run fix_missing_values to fill missing values
    ca.fix_missing_values(data, 'MinTemp')
    ca.fix_missing_values(data, 'MaxTemp')
    
    # Call the function with an invalid correlation type
    with pytest.raises(ValueError):
        ca.get_correlation_two_vars(data, 'MinTemp', 'MaxTemp', type_correlation='invalid')

def test_get_correlation_two_vars_missing_column(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Call the function with a missing column
    with pytest.raises(KeyError):
        ca.get_correlation_two_vars(data, 'NonExistentColumn', 'MaxTemp')

def test_get_correlation_two_vars_invalid_column_type(load_data):
    
    data = load_data  # Get dataFrame from fixture
    # NO need to run fix_missing_values to fill missing values
    
    # Call the function with an invalid correlation type
    with pytest.raises(ValueError):
        ca.get_correlation_two_vars(data, 'MinTemp', 'MaxTemp', type_correlation='invalid')

def test_plot_correlation(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Ensure there are no missing values in the columns
    ca.fix_missing_values(data, 'MinTemp')
    ca.fix_missing_values(data, 'MaxTemp')
    
    with patch('matplotlib.pyplot.show') as mock_show, \
            patch('matplotlib.pyplot.savefig') as mock_savefig, \
            patch('matplotlib.pyplot.scatter') as mock_scatter, \
            patch('matplotlib.pyplot.xlabel') as mock_xlabel, \
            patch('matplotlib.pyplot.ylabel') as mock_ylabel, \
            patch('matplotlib.pyplot.title') as mock_title:

        ca.plot_correlation(data, 'MinTemp', 'MaxTemp')

        # Check if the scatter plot was created with the correct data
        mock_scatter.assert_called_once_with(data['MinTemp'], data['MaxTemp'], alpha=0.5)
        
        # Check if the labels and title were set correctly
        mock_xlabel.assert_called_once_with('MinTemp')
        mock_ylabel.assert_called_once_with('MaxTemp')
        mock_title.assert_called_once_with('Scatterplot of MinTemp vs MaxTemp')
        
        # Check if the plot was saved as a PNG file
        mock_savefig.assert_called_once_with('plots/MinTemp_vs_MaxTemp_scatterplot.png')
        
        # Check if the plot was shown
        mock_show.assert_called_once()


def test_encode_categorical_data(load_data):
    data = load_data  # Get dataFrame from fixture
    dtypes = ['int64', 'int32', 'float64', 'float32']
    
    # Call the function
    column = 'Location'
    new_column = ca.encode_categorical_data(data, column)
    
    # Assert the new column is created
    assert new_column in data.columns
    assert data[new_column].dtype in dtypes  # Label encoding should result in integer values
    
    # Assert the original column is dropped
    assert 'Location' not in data.columns

def test_encode_categorical_data_empty():
    # Create an empty DataFrame
    data = pd.DataFrame({'Location': []})
    dtypes = ['int64', 'int32', 'float64', 'float32']
    
    # Call the function
    new_column = ca.encode_categorical_data(data, 'Location')
    
    # Assert the new column is created
    assert new_column in data.columns
    assert data[new_column].dtype in dtypes  # Label encoding should result in integer values
    
    # Assert the original column is dropped
    assert 'Location' not in data.columns

def test_encode_categorical_data_single_value():
    # Create a DataFrame with a single unique value
    data = pd.DataFrame({'Location': ['Sydney'] * 10})
    dtypes = ['int64', 'int32', 'float64', 'float32']
    
    # Call the function
    new_column = ca.encode_categorical_data(data, 'Location')
    
    # Assert the new column is created
    assert new_column in data.columns
    assert data[new_column].dtype in dtypes  # Label encoding should result in integer values
    
    # Assert the original column is dropped
    assert 'Location' not in data.columns
    
    # Assert all values in the new column are the same
    assert data[new_column].nunique() == 1
    assert data[new_column].unique()[0] == 0

def test_encode_categorical_data_multiple_values():
    # Create a DataFrame with multiple unique values
    data = pd.DataFrame({'Location': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide'] * 2})
    dtypes = ['int64', 'int32', 'float64', 'float32']
    
    # Call the function
    new_column = ca.encode_categorical_data(data, 'Location')
    
    # Assert the new column is created
    assert new_column in data.columns
    assert data[new_column].dtype in dtypes  # Label encoding should result in integer values
    
    # Assert the original column is dropped
    assert 'Location' not in data.columns
    
    # Assert the new column has the correct number of unique values
    assert data[new_column].nunique() == 5

def test_show_correlation_cities_rainfall(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Ensure there are no missing values in the columns
    ca.fix_missing_values(data, 'Location')
    ca.fix_missing_values(data, 'Rainfall')
    
    # Call the function
    corr, p_value, data_5_locs = ca.show_correlation_cities_rainfall(data, 'Location', 'Rainfall', type_correlation='pearson')
    
    # Assert the results
    assert isinstance(corr, float)  # Correlation should be a float
    assert isinstance(p_value, float)  # p-value should be a float
    assert -1 <= corr <= 1  # Correlation coefficient should be between -1 and 1

def test_show_correlation_cities_rainfall_five_location(load_data):
    data = load_data  # Get dataFrame from fixture
    
    # Ensure there are no missing values in the columns
    ca.fix_missing_values(data, 'Location')
    ca.fix_missing_values(data, 'Rainfall')
    
    # Call the function
    corr, p_value, data_5_locs = ca.show_correlation_cities_rainfall(data, 'Location', 'Rainfall')

    print(data_5_locs.columns)
    print(data_5_locs['Location_encoded'].nunique())
    # Check there are only 5 Location_encoded in the data
    assert data_5_locs['Location_encoded'].nunique() == 5



if __name__ == '__main__':
    pytest.main()