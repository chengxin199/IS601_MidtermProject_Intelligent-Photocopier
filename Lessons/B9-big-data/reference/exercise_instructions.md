---
title: introduction to big data - Exercise Instructions
layout: layouts/course.njk
courseId: B9-big-data
tags:
  - exercises
  - practice
date: 2025-12-08T15:29:06.345107
---
## Exercise 1: Loading and Exploring Big Data
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes  

### Objective
Implement a function to load a CSV file containing large datasets and perform basic exploratory data analysis (EDA) by displaying the number of rows, columns, and the first few rows of the dataset.

### Starter Code
```python
import pandas as pd

def load_and_explore_data(file_path):
    # TODO: Load the CSV file into a Pandas DataFrame
    # TODO: Return the number of rows, columns, and the first 5 rows of the DataFrame
    pass
```

### Requirements
- Use `pandas` to load the CSV file.
- Return a tuple containing:
  - The number of rows
  - The number of columns
  - The first 5 rows of the DataFrame
- Handle the case where the file does not exist by returning an appropriate message.

### Test Cases
```python
# Example test cases
assert load_and_explore_data('data.csv') == (1000, 10, expected_dataframe_head)
assert load_and_explore_data('non_existent_file.csv') == "File not found."
```

### Hints
- Use `pd.read_csv()` to load the CSV file.
- Use `.shape` to get the dimensions of the DataFrame.
- Use `.head()` to get the first few rows.

---

## Exercise 2: Data Cleaning
**Difficulty:** Intermediate  
**Time Estimate:** 40 minutes  

### Objective
Create a function that takes a DataFrame and cleans it by removing rows with missing values and duplicates.

### Starter Code
```python
def clean_data(df):
    # TODO: Remove rows with any missing values
    # TODO: Remove duplicate rows
    # TODO: Return the cleaned DataFrame
    pass
```

### Requirements
- Ensure that any row with missing values is removed.
- Ensure that duplicate rows are removed.
- Return the cleaned DataFrame.

### Test Cases
```python
# Example test cases
import pandas as pd

data = {
    'A': [1, 2, None, 4, 5, 2],
    'B': [None, 2, 3, 4, 5, 2]
}
df = pd.DataFrame(data)

cleaned_df = clean_data(df)
assert cleaned_df.shape[0] == 4  # Should have 4 rows after cleaning
```

### Hints
- Use `df.dropna()` to remove rows with missing values.
- Use `df.drop_duplicates()` to remove duplicate rows.

---

## Exercise 3: Basic Data Aggregation
**Difficulty:** Intermediate  
**Time Estimate:** 45 minutes  

### Objective
Implement a function that takes a cleaned DataFrame and calculates the mean and median of a specified numeric column, grouped by a categorical column.

### Starter Code
```python
def aggregate_data(df, numeric_col, categorical_col):
    # TODO: Group the DataFrame by the categorical column and calculate mean and median
    # TODO: Return a new DataFrame with the results
    pass
```

### Requirements
- Accept `numeric_col` and `categorical_col` as parameters.
- Return a DataFrame containing the mean and median for the numeric column grouped by the categorical column.

### Test Cases
```python
# Example test cases
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 10, 30, 20, 40]
}
df = pd.DataFrame(data)

result_df = aggregate_data(df, 'Values', 'Category')
assert result_df.shape[0] == 3  # Should have 3 unique categories
assert result_df['mean'].iloc[0] == 15  # Mean for category 'A'
```

### Hints
- Use `df.groupby()` to group by the categorical column.
- Use `.agg()` to calculate multiple statistics (mean and median).

---

## Exercise 4: Visualizing Data
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes  

### Objective
Write a function that takes a DataFrame and creates a bar plot of the mean values of a specified numeric column grouped by a categorical column.

### Starter Code
```python
import matplotlib.pyplot as plt

def plot_data(df, numeric_col, categorical_col):
    # TODO: Group the DataFrame by the categorical column and calculate the mean
    # TODO: Create a bar plot of the mean values
    pass
```

### Requirements
- Use `matplotlib` to create the plot.
- The x-axis should represent the categories, and the y-axis should represent the mean values.
- Ensure the plot is labeled appropriately.

### Test Cases
```python
# Example test cases
data = {
    'Category': ['A', 'A', 'B', 'B'],
    'Values': [10, 20, 15, 25]
}
df = pd.DataFrame(data)

# Call the function to generate the plot
plot_data(df, 'Values', 'Category')
# Check if a plot is generated but cannot assert as it's a visual output
```

### Hints
- Use `df.groupby().mean()` to calculate the mean values.
- Use `plt.bar()` to create the bar plot.

---

## Exercise 5: Exporting the Cleaned Data
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes  

### Objective
Implement a function that takes a cleaned DataFrame and exports it to a new CSV file.

### Starter Code
```python
def export_to_csv(df, output_file):
    # TODO: Export the DataFrame to CSV format
    pass
```

### Requirements
- Use `pandas` to write the DataFrame to a CSV file.
- Ensure that the function handles file writing errors gracefully.

### Test Cases
```python
# Example test cases
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

export_to_csv(df, 'output.csv')
# Check if the file is created successfully (manual check)
```

### Hints
- Use `df.to_csv()` to write the DataFrame to a CSV file.
- Use a try-except block to catch any potential file writing errors.