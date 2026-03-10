"""
DataFrame Creation from 2D List Module

This module provides functionality to convert a 2D list (list of lists) containing 
student data into a structured pandas DataFrame. This is useful for transforming 
raw data into a format suitable for data analysis and manipulation.

The module demonstrates:
1. Converting a 2D list into a pandas DataFrame
2. Assigning meaningful column names to the DataFrame
3. Working with structured student data (ID and age information)
4. Type hinting for better code clarity and IDE support

Input Format:
The function expects a 2D list where each inner list contains two integers:
- First element: student ID (unique identifier for the student)
- Second element: student age (age of the student in years)

Example:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
"""

import pandas as pd  # Importing pandas for DataFrame creation and data manipulation


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    """
    Convert a 2D list of student data into a pandas DataFrame.
    
    This function takes a list of student records (where each record contains 
    a student ID and age) and creates a properly formatted DataFrame with 
    named columns for easy data access and manipulation.
    
    Parameters:
    -----------
    student_data : list[list[int]]
        A 2D list (list of lists) where each inner list contains exactly two integers:
        - student_data[i][0]: Student ID (integer, should be unique)
        - student_data[i][1]: Student age (integer, in years)
        
        Example:
        [[1, 15], [2, 11], [3, 11], [4, 20]]
    
    Returns:
    --------
    pd.DataFrame
        A pandas DataFrame with two columns:
        - 'student_id': Contains the student IDs
        - 'age': Contains the student ages
        
        The resulting DataFrame will have the same number of rows as the input list.
        
        Example output:
           student_id  age
        0           1   15
        1           2   11
        2           3   11
        3           4   20
    
    Example:
    --------
    >>> data = [[1, 15], [2, 11], [3, 11], [4, 20]]
    >>> df = createDataframe(data)
    >>> print(df)
       student_id  age
    0           1   15
    1           2   11
    2           3   11
    3           4   20
    """
    
    # Define the column names for the DataFrame
    # These names correspond to the data in the 2D list:
    # - "student_id" for the first element of each inner list
    # - "age" for the second element of each inner list
    column_names = ["student_id", "age"]
    
    # Create the DataFrame using the 2D list and the specified column names
    # pd.DataFrame() constructor accepts:
    #   - data: the 2D list containing the student records
    #   - columns: list of column names to assign to each column
    # The resulting DataFrame maps each inner list to a row in the DataFrame
    df = pd.DataFrame(student_data, columns=column_names)
    
    # Return the newly created DataFrame
    return df


# ============================================================================
# EXAMPLE USAGE SECTION: Creating and displaying a DataFrame from student data
# ============================================================================

# Create sample student data as a 2D list
# Each inner list represents one student with their ID and age
# This simulates a real-world scenario with 4 students
student_data = [
    [1, 15],    # Student ID 1, age 15
    [2, 11],    # Student ID 2, age 11
    [3, 11],    # Student ID 3, age 11
    [4, 20]     # Student ID 4, age 20
]

# Call the function to create a DataFrame from the student data
# This converts the raw 2D list into a structured, labeled DataFrame
df = createDataframe(student_data)

# Display the resulting DataFrame
# The output will be a nicely formatted table with student_id and age columns
print(df)