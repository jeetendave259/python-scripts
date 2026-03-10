# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# Write a solution to select the name and age of the student with student_id = 101.

# The result format is in the following example.

 

# Example 1:
# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |
# +------------+---------+-----+
# Output:
# +---------+-----+
# | name    | age | 
# +---------+-----+
# | Ulysses | 13  |
# +---------+-----+
# Explanation:
# Student Ulysses has student_id = 101, we select the name and age.

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Select the name and age of the student with student_id = 101 from the given DataFrame.
    
    This function filters the input DataFrame to find the row where the student_id is 101,
    and then selects only the 'name' and 'age' columns for that specific student.
    
    Parameters:
    -----------
    students : pd.DataFrame
        A pandas DataFrame containing student information with columns:
        - student_id: Unique identifier for each student (int)
        - name: Student name (str/object)
        - age: Student age (int)    
        
    Returns:
    --------
    pd.DataFrame
        A DataFrame containing the 'name' and 'age' of the student with student_id = 101.
        If no student with student_id = 101 is found, an empty DataFrame with columns 'name' and 'age' will be returned.        
        Example output:
           name  age
        0  Ulysses   13
    Example:
    --------
    >>> data = {
    ...     'student_id': [101, 53, 128, 3],
    ...     'name': ['Ulysses', 'William', 'Henry', 'Henry
    ...     'age': [13, 10, 6, 11]
    ... }
    >>> students = pd.DataFrame(data)
    >>> selectData(students)
              name  age
        0  Ulysses   13
    """
    # Filter the DataFrame to find the row where student_id is 101
    # Then select only the 'name' and 'age' columns for that row
    result = students[students['student_id'] == 101][['name', 'age']]
    
    return result

# ============================================================================
# DEMONSTRATION SECTION: Sample data and DataFrame creation
# ============================================================================
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'student_id': [101, 53, 128, 3],
        'name': ['Ulysses', 'William', 'Henry', 'Henry'],
        'age': [13, 10, 6, 11]
    }
    
    # Create a DataFrame from the sample data
    students_df = pd.DataFrame(data)
    
    # Call the function to select the name and age of the student with student_id = 101
    result_df = selectData(students_df)
    
    # Print the result
    print(result_df)