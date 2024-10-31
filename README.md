# CS 4580: Introduction to Data Correlations 


**Note: All function signatures for the upcoming tasks have already been defined in the `ca.py` file. This is the file that is going to contain all your work.**



## Task 0: Setup Conda Virtual Environment

Before starting the data wrangling tasks, make sure you have a `new conda` virtual environment setup. The environment should be named `assignment4`.

- Follow the instructions provided in [SettingVirtualEnv](SettingVirtualEnv.md) to set up the virtual environment.
- Once the environment is activated, install the necessary libraries by running the `requirements.txt` file (which includes Pandas and any other dependencies).


## Task 1: Accessing the Dataset

For this assignment, you will be working with a census dataset from `Kaggle`. The dataset is provided in a zip file.  See [Data Info](data/README.md) for details.

Note: The data should be downloaded and extracted in the `data/` folder.

## Task 2: Load Dataset into a DataFrame

Write a function called `load_data(file_path)` that:
- Loads census data from a CSV file.
- Args: `file_path (str)`: The path to the CSV file containing the census data.
- Returns: `pandas.DataFrame`: A DataFrame containing the census data with rows where the state is 'Puerto Rico' removed.


#### Print Results
For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASK 2: Load census data into a DataFrame
    print(f'Task 2: Load weather data into a DataFrame')
    census_data_file = 'data/weatherAUS.csv'
    data = load_data(census_data_file)
    print(f'Loaded {len(data)} records')
```



## Task 3: Get the Start and End Dates

In this task you will get data's start and end dates from the data set

Write a function called `get_start_end_date(data)` that:
- Get the start and end dates from the given weather data. This function converts the `Date` column in the provided DataFrame to datetime objects and returns the minimum and maximum dates.

- Args: `data (pd.DataFrame)`: A DataFrame containing a 'Date' column with date information.

- Returns: `tuple`: A tuple containing the earliest and latest dates in the 'Date' column.

### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASk 3: Print (to the console) the start to end of the time in days, months, and years.
    print(f'\nTask 3: Print the start and end of the time in days, months, and years')
    min_date, max_date = get_start_end_date(data)
    print(f'Start Date: {min_date}')
    print(f'End Date: {max_date}')

```

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k test_get_start_end_date
```

## Task 4: Get Average Minimum Temperatures

In this task you will calculate the average minimum temperature for each month.

Write a function called `get_avg_min_temp_by_month(data)` that:
- This function takes a DataFrame containing weather data, converts the 'Date' column to datetime, extracts the month from the 'Date', and then calculates the average minimum temperature for each month.

- Args: `data (pd.DataFrame)`: A DataFrame containing weather data

- Returns: `pd.Series`: A Series with the average minimum temperature for each month, indexed by month (1-12).

### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASK 4: Print (to the console) the average MinTemp based on month (you should display 12 values).
    print(f'\nTask 4: Print the average MinTemp based on month')
    avg_min_temp = get_avg_min_temp_by_month(data)
    print(f'Average MinTemp by Month: {avg_min_temp}')
```

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k  test_get_avg_min_temp_by_month
```

## Task 5: Plot Data
In this task, you will plot the average minimum temperature by month calculated in the previous Task.

Write a function called `plot_avg_min_temp_by_month(avg_min_temp)` that:
- Displays the previous Task data in a bar chart (or histogram) using `matplotlib`. The function creates a bar plot with the months on the x-axis and the average minimum temperatures on the y-axis. 
- Args: `avg_min_temp (pd.Series)`: A pandas Series where the index represents the months and the values represent the average minimum temperatures.
- The plot is saved in the `plots/` folder as `avg_min_temp_by_month.png` and displayed in a non-blocking manner.


### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # Task 5: Display this information in a bar chart (or histogram) using the 'matplotlib' or 'plotly' package. 
    # The x-axis should be the month and the y-axis should be the average MinTemp.
    print(f'\nTask 5: Display the average MinTemp by month in a bar chart')
    plot_avg_min_temp_by_month(avg_min_temp)
```

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k test_plot_avg_min_temp_by_month
```

## Task 6: Get Unique Cities

In this task, your will report the number of `unique cities` in the dataset.

Write a function called `get_unique_cities(data)` that:
- Returns the number of unique cities in the dataset.
- Args: `data (pandas.DataFrame)`: The dataset containing weather data with a 'Location' column.
- Returns: `int`: The number of unique cities in the `Location` column of the dataset.

### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASK 6: Get Unique Cities
    print(f'\nTask 6: Get Unique Cities')
    unique_cities = get_unique_cities(data)
    print(f'Unique Cities: {unique_cities}')
```

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k  test_get_unique_cities
```

## Task 7: Get Top Rainiest Cities

In this task, your will prints the top `n` rainiest cities based on the total rainfall.

Write a function called `print_top_rainiest_cities(data, n=5)` that:
- Takes Args:
    - `data (pandas.DataFrame)`: The dataset containing weather data with `Location` and `Rainfall` columns.
    - `n (int)`: The number of top rainiest cities to print.
- Returns: `list`: A list of the top 'n' rainiest cities based on total rainfall.

### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASK 7: Print out the top five rainiest cities in the dataset.
    total = 5
    print(f'\nTask 7: Print the top five rainiest cities in the dataset')
    rainiest_cities = print_top_rainiest_cities(data, total)
    print(f'Top {total} Rainiest Cities: {rainiest_cities}')
```

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k test_print_top_rainiest_cities
```


## Task 8: Print Univariate Values 

In this task, you will get the most common `univariate` values (e.g mean of Pressure9am, mode of Humidity, etc.). Print out at least five, but feel free to print out more. The most important point is to gain insight into the data.


Write a function called `print_univariate_values(data)` that:
- Prints various univariate statistics for a given dataset.
` Parameters: `data (DataFrame)`: A pandas DataFrame containing weather data with the following columns:
- The function prints the following statistics:
    - `Mean` of 'Pressure9am'
    - `Mode` of 'Humidity9am'
    - `Median` of 'WindGustSpeed'
    - `Standard deviation` of 'Temp3pm'
    - `75th percentile` of 'Rainfall'
    - `Minimum` of 'MaxTemp'
    - `Maximum` of 'MinTemp'
    - `Range` of 'WindSpeed9am' (max - min)
    - `Variance` of 'Evaporation'
    - `Skewness` of 'Sunshine'

### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASK 8: Print out different univariate values 
    print(f'\nTask 8: Print univariate values')
    print_univariate_values(data)

```
Sample Output
```bash
# Make sure your output matches this format, up to 2 decimal places.
Mean Pressure9am: 1017.65
Mode Humidity9am: 99.00
Median WindGustSpeed: 39.00
Standard Deviation Temp3pm: 6.94
75th Percentile Rainfall: 0.80
Minimum MaxTemp: -4.80
Maximum MinTemp: 33.90
Range WindSpeed9am: 130.00
Variance Evaporation: 17.59
Skewness Sunshine: -0.50
```
Note: Format all floats to 2 decimal places. 

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k test_print_univariate_values
```

## Task 9: Fix Missing Values

In this task, you will fix missing values in the dataset. 

Write a function called `fix_missing_values(data, column)` that:

- Checks if the specified column in the DataFrame has any missing values (NaN or inf).
    If missing values are found, they are filled with the `median` value of that column.
- Parameters:
    - `data (pandas.DataFrame)`: The DataFrame containing the data.
    - `column (str)`: The name of the column to check and fix missing values.
- Returns: None: The function modifies the DataFrame `in place`.

### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASK 9: Fix missing values
    print(f'\nTask 9: Fix missing values for MinTemp and Rainfall')
    col1 = 'MinTemp'
    fix_missing_values(data, col1)
    col2 = 'Rainfall'
    fix_missing_values(data, col2)
```

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k test_fix_missing_values
```

## Task 10A: First Correlation

In this task, calculate the `correlation` between `MinTemp` and `RainFall`. 

Write a function called `def get_correlation_two_vars(data, var1, var2, type_correlation='pearson')` that:
- Calculate the correlation between two variables in a dataset.
- Parameters:
    - `data (pandas.DataFrame)`: The dataset containing the variables.
    - `var1 (str)`: The name of the first variable.
    - `var2 (str)`: The name of the second variable.
    - `type_correlation (str, optional)`: The type of correlation to compute. Options are 'pearson' (`default`) and 'spearman'.
- Returns: `tuple`: A tuple containing the `correlation coefficient` and the `p-value`.
- Raises:
    - `KeyError`: If var1 or var2 are not found in the dataset.
    - `KeyError`: If var1 or var2 are not of `dtype` = `['int64', 'int32', 'float64', 'float32']`
    - `ValueError`: If the type_correlation is not 'pearson' or 'spearman'.
    """
        
### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASK 10A: Show the correlation between MinTemp and Rainfall
    print(f'\nTask 10: Show the correlation between MinTemp and Rainfall')
    correlations = ['pearson', 'spearman']
    for correlation in correlations:
        corr, p_value  = get_correlation_two_vars(data, col1, col2, type_correlation=correlation)
        # Display p_value in scientific notation up to -22
        print(f'{correlation.capitalize()} Correlation ({col1}, {col2}): {corr:.6f}. P-value: {p_value:.21e}')   
```

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k  test_show_correlation_two_vars
```


NOTE: This is a hard to test scenario. The test cases will test that you have the correct types, but not the actual values. Make sure you explain this section well in your video. 

### Task 10B: Explain Results
Explain the correlation in the console as print statements.
- What is the meaning of the `correlation` result
- What is the meaning of the `p_value` result
        
### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 
```python
        # Task 10B: Explain the correlation in the console
```

Note: No testing code for this. Make sure you document your findings!

### Task 10C: Plot Correlation

In this task, you will write a function called `def plot_correlation(data, var1, var2, type_correlation='pearson')` that:

- Plots a `scatterplot` to visualize the correlation between two variables in a dataset.
- Parameters:
    - `data (pandas.DataFrame)`: The dataset containing the variables to be plotted.
    - `var1 (str)`: The name of the first variable (column) in the dataset.
    - `var2 (str)`: The name of the second variable (column) in the dataset type_correlation (str, optional): The type of correlation to be considered. Default is 'pearson'.
- Returns: None

Notes:
 - The scatterplot is saved as a `PNG` file in the `plots/` directory with a filename format:  '{var1}_vs_{var2}_scatterplot_{type_correlation}.png'.
- The plot is displayed in a `non-blocking` manner.
- Include a `title`, `xlabel`, `ylabel`, and `grid=True`

### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # TASK 10C: Plot the correlation
    plot_correlation(data, col1, col2, type_correlation='pearson')
```


### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Run function test
pytest -k  test_plot_correlation
```

## Task 11: Second Correlation

In this task, you will defined a funciton called `def show_correlation_cities_rainfall(data, col1, col2, type_correlation='pearson')` that:

- Calculate and display the correlation between rainfall data of randomly selected locations. 
- You will create a new dataframe `randomly` selecting `5 locations`
- Parameters:
    - `data_orig (pd.DataFrame)`: The original dataframe containing the data.
    - `col1 (str)`: The name of the first column to be used in the correlation.
    - `col2 (str)`: The name of the second column to be used in the correlation.
        type_correlation (str, optional): The type of correlation to compute. Default is 'pearson'. 
- Returns: `tuple`: A tuple containing the `correlation` value, the `p-value`, and a `new DataFrame` with the encoded data with 5 Locations only. 


In order to complete this task, you need two additional wrangling steps: 
- Checks if the `dtype` is an `object`. If it is, then do the next step:

- Create another function called `def encode_categorical_data(data, column)` that:
`Encodes` a categorical column in the given DataFrame as `numeric` using Label Encoding.
- The `original` column is dropped from the DataFrame and `replaced` with the new encoded column.
- A warning message is printed indicating that the column must be numeric to calculate correlation.

- Parameters:
    - `data (pd.DataFrame)`: The DataFrame containing the data.
    - `column (str)`: The name of the column to be encoded.

- Returns: `str`: The name of the `new column` containing the encoded values. Using the following naming convention: `new_label = f'{column}_encoded'`

### Print Results

For illustration purposes, you may uncomment the following code from your `main()` function: 

```python
    # Task 11: Second correlation
    correlation = 'pearson'
    col1 = 'Location'
    col2 = 'Rainfall'
    print(f'\nTask 11: Show the correlation between {col1} and {col2}')   
    corr, p_value = show_correlation_cities_rainfall(data, col1, col2, type_correlation=correlation)
    print(f'{correlation.capitalize()} Correlation ({col1}, {col2}): {corr:.6f}. P-value: {p_value:.21e}')   
```

### Testing Instructions:

Once you've implemented the function, you can test it by running the following command in your terminal:

```bash
# Test categorical_data function
pytest -k test_encode_categorical_data

# Test show correlation_cities_rainfall
pytest -k test_correlation_cities_rainfall
```

## Video Walkthrough Instructions

As part of your submission, you are required to record a video walkthrough that includes the following:

- Demo Running the Code:
  - Show your code running in your local environment.
  - Ensure that the program executes without errors, and demonstrate how it handles the tasks outlined in the assignment.
- Demo Passing All Test Cases:
  - Run the provided test cases (if applicable) and demonstrate that your code passes all of them.
  - If your assignment includes pytest test cases, show the terminal output with all tests passing.
- Quick Explanation of Your Approach:
  - For each task, give a brief explanation of how you approached and solved the problem.
  - Focus on key decisions or challenges you faced and how you addressed them.

### Video Walkthrough Submission Guidelines:

- The video should be clear and easy to follow, with both the terminal and code editor visible.
- You may use screen recording software such as Zoom, OBS, or any other tool of your choice.
- Upload your video to `Canvas`, and provide the link to your GitHub Repo as a comment to your submission. 

#### Submission Checklist:

- [ ] Complete all tasks in the ca.py file.
- [ ] Record a video walkthrough that includes a code demo, test case demo, and explanations.
- [ ] Upload the video and submit the link to the GitHub Repo along with your assignment.
