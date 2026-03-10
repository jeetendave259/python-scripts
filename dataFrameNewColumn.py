# DataFrame employees
# +-------------+--------+
# | Column Name | Type.  |
# +-------------+--------+
# | name        | object |
# | salary      | int.   |
# +-------------+--------+
# A company plans to provide its employees with a bonus.

# Write a solution to create a new column name bonus that contains the doubled values of the salary column.

# The result format is in the following example.

 

# Example 1:

# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Piper   | 4548   |
# | Grace   | 28150  |
# | Georgia | 1103   |
# | Willow  | 6593   |
# | Finn    | 74576  |
# | Thomas  | 24433  |
# +---------+--------+
# Output:
# +---------+--------+--------+
# | name    | salary | bonus  |
# +---------+--------+--------+
# | Piper   | 4548   | 9096   |
# | Grace   | 28150  | 56300  |
# | Georgia | 1103   | 2206   |
# | Willow  | 6593   | 13186  |
# | Finn    | 74576  | 149152 |
# | Thomas  | 24433  | 48866  |
# +---------+--------+--------+
# Explanation: 
# A new column bonus is created by doubling the value in the column salary.

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column 'bonus' in the DataFrame by doubling the values of the 'salary' column.
    
    This function takes a DataFrame containing employee information, specifically the 'salary' column,
    and computes a new column called 'bonus' where each value is twice the corresponding value in 'salary'.
    
    Parameters:
    -----------
    employees : pd.DataFrame
        A pandas DataFrame containing employee information with at least the following columns:
        - name: Employee name (str/object)
        - salary: Annual salary (int)
    
    Returns:
    --------
    pd.DataFrame
        A new DataFrame that includes all original columns plus an additional 'bonus' column.
        The 'bonus' column contains values that are double those in the 'salary' column.
        
        Example output:
           name    salary   bonus
        0  Piper   4548     9096
        1  Grace   28150    56300
        2  Georgia 1103     2206
        3  Willow  6593     13186
        4  Finn    74576    149152
        5  Thomas  24433    48866   
    Example:
    --------
    >>> data = {
    ...     'name': ['Piper', 'Grace', 'Georgia', 'Willow
    ...     'salary': [4548, 28150, 1103, 6593, 74576, 24433]
    ... }
    >>> employees = pd.DataFrame(data)
    >>> createBonusColumn(employees)
              name    salary   bonus
        0    Piper     4548     9096
        1    Grace     28150    56300
        2  Georgia     1103     2206
        3   Willow     6593     13186
        4     Finn     74576    149152
        5   Thomas     24433    48866
    """
    # Create a new column 'bonus' by doubling the values in the 'salary' column
    # This is done using vectorized operations, which are efficient in pandas
    employees['bonus'] = employees['salary'] * 2
    
    # Return the modified DataFrame with the new 'bonus' column included
    return employees

# ============================================================================
# DEMONSTRATION SECTION: Sample data and DataFrame creation
# ============================================================================
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
        'salary': [4548, 28150, 1103, 6593, 74576, 24433]
    }
    
    # Create a DataFrame from the sample data
    employees = pd.DataFrame(data)
    
    # Call the function to create the bonus column and print the result
    result_df = createBonusColumn(employees)
    print(result_df)