---
title: introduction to pandas python - Exercise Instructions
layout: layouts/course.njk
courseId: P5-pandas-python
tags:
  - exercises
  - practice
date: 2025-12-08T17:02:51.678849
---
## Exercise 1: DataFrame Basics
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes

### Objective
Create a Pandas DataFrame from a dictionary and perform basic operations such as displaying the DataFrame, accessing columns, and calculating basic statistics.

### Starter Code
```python
import pandas as pd

def create_dataframe():
    # TODO: Create a DataFrame from the following dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [70000, 80000, 120000]
    }
    
    df = pd.DataFrame(data)  # Create DataFrame
    return df

# Call the function and print the DataFrame
df = create_dataframe()
print(df)
```

### Requirements
- Create the DataFrame as shown in the starter code.
- Access the 'Name' column and return it as a list.
- Calculate the mean salary and return it.

### Test Cases
```python
df = create_dataframe()
assert df['Name'].tolist() == ['Alice', 'Bob', 'Charlie']
assert df['Salary'].mean() == 90000.0
```

### Hints
- Use `df['ColumnName']` to access specific columns.
- Use `df.mean()` to calculate the mean of numeric columns.

---

## Exercise 2: DataFrame Indexing and Filtering
**Difficulty:** Intermediate  
**Time Estimate:** 20 minutes

### Objective
Filter the DataFrame to find employees older than a certain age and calculate the average salary of the filtered results.

### Starter Code
```python
import pandas as pd

def filter_dataframe(df, age_threshold):
    # TODO: Filter the DataFrame for employees older than age_threshold
    filtered_df = df[df['Age'] > age_threshold]
    
    # TODO: Calculate the average salary of the filtered results
    average_salary = filtered_df['Salary'].mean()
    
    return average_salary

# Sample DataFrame to use for filtering
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [70000, 80000, 120000, 90000]
}

df = pd.DataFrame(data)
```

### Requirements
- Filter the DataFrame for employees older than `age_threshold`.
- Calculate the average salary of the filtered DataFrame and return it.

### Test Cases
```python
assert filter_dataframe(df, 30) == 105000.0  # Only Charlie and David
assert filter_dataframe(df, 25) == 95000.0    # All employees
```

### Hints
- Use boolean indexing to filter the DataFrame.
- Remember to use `mean()` on the filtered DataFrame's salary column.

---

## Exercise 3: Grouping and Aggregating Data
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes

### Objective
Group the DataFrame by a specific column and calculate aggregate statistics for another column.

### Starter Code
```python
import pandas as pd

def group_and_aggregate(df):
    # TODO: Group the DataFrame by 'Age' and calculate the total salary for each age group
    aggregated_data = df.groupby('Age')['Salary'].sum().reset_index()
    
    return aggregated_data

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 30, 25],
    'Salary': [70000, 80000, 120000, 90000, 75000]
}

df = pd.DataFrame(data)
```

### Requirements
- Group the DataFrame by the 'Age' column.
- Calculate the total salary for each age group.
- Return the result as a new DataFrame.

### Test Cases
```python
result = group_and_aggregate(df)
expected_output = pd.DataFrame({
    'Age': [25, 30, 35],
    'Salary': [145000, 170000, 120000]
})
pd.testing.assert_frame_equal(result, expected_output)
```

### Hints
- Use `groupby()` to group the DataFrame.
- Use `sum()` to calculate the total salary.

---

## Exercise 4: Handling Missing Data
**Difficulty:** Advanced  
**Time Estimate:** 30 minutes

### Objective
Identify and handle missing data in a DataFrame by filling missing values with the mean of their respective columns.

### Starter Code
```python
import pandas as pd
import numpy as np

def handle_missing_data(df):
    # TODO: Fill missing values with the mean of their respective columns
    df_filled = df.fillna(df.mean())
    
    return df_filled

# Sample DataFrame with NaN values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 35, 40],
    'Salary': [70000, 80000, np.nan, 90000]
}

df = pd.DataFrame(data)
```

### Requirements
- Identify any NaN values in the DataFrame.
- Fill those NaN values with the mean of their respective columns.
- Return the modified DataFrame.

### Test Cases
```python
df_filled = handle_missing_data(df)
expected_output = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25.0, 33.333333, 35.0, 40.0],
    'Salary': [70000.0, 80000.0, 83333.333333, 90000.0]
})
pd.testing.assert_frame_equal(df_filled, expected_output, check_dtype=False)
```

### Hints
- Use `isna()` to check for missing values.
- The `fillna()` function can be used to replace NaN values with the mean of the column.

---

These exercises progressively build on each other, introducing key concepts of Pandas in practical scenarios, while reinforcing understanding through coding and testing.