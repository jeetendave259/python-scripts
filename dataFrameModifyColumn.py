# DataFrame employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | salary      | int    |
# +-------------+--------+
# A company intends to give its employees a pay rise.

# Write a solution to modify the salary column by multiplying each salary by 2.

# The result format is in the following example.

 

# Example 1:

# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 19666  |
# | Piper   | 74754  |
# | Mia     | 62509  |
# | Ulysses | 54866  |
# +---------+--------+
# Output:
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
# +---------+--------+
# Explanation:
# Every salary has been doubled.

"""
The module demonstrates:
1. Modifying a specific column in a pandas DataFrame using vectorized operations
2. Type hinting with Python's typing module for better code clarity and maintainability 
3. Practical example with employee salary data to illustrate the concept of column modification
Expected DataFrame Structure (employees):
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+    
Use Cases:
- Adjusting salary data for pay raises or corrections       
- Modifying numerical data in a DataFrame based on specific business rules
- Performing bulk updates to a column without using loops for efficiency
"""

import pandas as pd  # Importing pandas for DataFrame operations and data manipulation

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Modify the 'salary' column in the DataFrame by multiplying each salary by 2.
    
    This function uses vectorized operations provided by pandas to efficiently update
    the 'salary' column without the need for explicit loops. It takes advantage of
    pandas' ability to perform element-wise operations on DataFrame columns, resulting
    in cleaner and faster code.
    
    Parameters:
    -----------
    employees : pd.DataFrame
        A pandas DataFrame containing employee information with columns:
        - name: Employee name (str/object)
        - salary: Annual salary (int)
        
    Returns:
    --------
    pd.DataFrame
        A new DataFrame with the 'salary' column modified by multiplying each salary by 2.
        The structure and column names are preserved.
        
        Example:
           name    salary
        0   Jack    39332
        1   Piper   149508
        2   Mia     125018
        3   Ulysses 109732
    Example:
    --------
    >>> import pandas as pd     
    >>> data = {
    ...     'name': ['Jack', 'Piper', 'Mia', 'U
lysses'],
    ...     'salary': [19666, 74754, 62509, 54866]
    ... }
    >>> employees = pd.DataFrame(data)
    >>> modifySalary(employees)
           name    salary
        0   Jack    39332
        1   Piper   149508
        2   Mia     125018
        3   Ulysses 109732
    """
    # Use vectorized operations to modify the 'salary' column by multiplying each value by 2
    employees['salary'] = employees['salary'] * 2
    
    # Display the modified DataFrame for verification and debugging purposes
    print("Modified DataFrame with updated salaries:")
    print(employees)
    
    return employees