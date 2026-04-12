# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# There are some rows having missing values in the name column.

# Write a solution to remove the rows with missing values.

# The result format is in the following example.

 

# Example 1:

# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 217        | None    | 19  |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# +------------+---------+-----+
# Output:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 779        | Georgia | 20  | 
# | 849        | Willow  | 14  | 
# +------------+---------+-----+
# Explanation: 
# Student with id 217 havs empty value in the name column, so it will be removed.

"""
The module demonstrates:
1. Removing rows with missing values in a specific column using pandas
2. Type hinting with Python's typing module for better code clarity and IDE support
3. Practical example with student data containing missing names in the DataFrame
Expected DataFrame Structure (students):
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Use Cases:
- Cleaning datasets by removing incomplete records
- Ensuring data integrity for analysis and modeling
- Handling missing data in a structured way
"""

import pandas as pd  # Importing pandas for DataFrame operations and data manipulation

def dropMissingNames(students: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows from the DataFrame that have missing values in the 'name' column.
    
    This function uses pandas' dropna() method to efficiently remove rows with NaN values
    in the specified column. In this case, it targets the 'name' column to ensure that
    all remaining records have valid names for further analysis or processing.
    
    Parameters:
    -----------
    students : pd.DataFrame
        A pandas DataFrame containing student information with columns:
        - student_id: Unique identifier for each student (int)
        - name: Student name (str/object), may contain missing values (NaN)
        - age: Student age (int)
    
    Returns:
    --------
    pd.DataFrame
        A new DataFrame with rows containing missing values in the 'name' column removed.
        The structure and column names are preserved.
        
        Example output:
           student_id     name  age
        0          32   Piper    5
        2         779 Georgia   20
        3         849 Willow   14
    
    Example:
    --------
    >>> import pandas as pd
    >>> data = {
    ...     'student_id': [32, 217, 779, 849],
    ...     'name': ['Piper', None, 'Georgia', 'Willow'],
    ...     'age': [5, 19, 20, 14]
    ... }
    >>> df = pd.DataFrame(data)
    >>> dropMissingNames(df)
       student_id     name  age
    0          32   Piper    5
    2         779 Georgia   20
    3         849 Willow   14
    """
    
    # Use dropna to remove rows where 'name' is NaN (missing)
    cleaned_students = students.dropna(subset=['name'])
    
    # Display the cleaned DataFrame for verification and debugging purposes
    print("DataFrame after dropping rows with missing names:")
    print(cleaned_students)
    
    # Return the cleaned DataFrame with missing names removed
    return cleaned_students

