"""
DataFrame First Three Rows Selector Module

This module provides functionality to extract and display the first 3 rows of a 
pandas DataFrame. This is useful for quick data inspection and verification of 
DataFrame content without loading the entire dataset.

The module demonstrates:
1. Using pandas DataFrame.head() method for row selection
2. Type hinting with Python's typing module for code clarity
3. Practical example with employee data

Expected DataFrame Structure (employees):
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+

Use Cases:
- Quick data preview without scrolling through large datasets
- Verify data structure and content
- Sample inspection before processing
- Data quality checks
"""

import pandas as pd  # Importing pandas for DataFrame operations


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Extract and return the first 3 rows from a pandas DataFrame.
    
    This function uses pandas' head() method to efficiently retrieve the first N rows
    of a DataFrame. It's particularly useful for quick data inspection, verification,
    and previewing large datasets without loading all rows into memory at once.
    
    Parameters:
    -----------
    employees : pd.DataFrame
        A pandas DataFrame containing employee information with columns:
        - employee_id: Unique identifier for each employee (int)
        - name: Employee name (str/object)
        - department: Department assignment (str/object)
        - salary: Annual salary (int)
    
    Returns:
    --------
    pd.DataFrame
        A new DataFrame containing only the first 3 rows from the input DataFrame.
        The structure and column names are preserved.
        
        Example:
           employee_id     name   department  salary
        0            1    Alice           HR   70000
        1            2      Bob  Engineering   80000
        2            3  Charlie    Marketing   75000
    
    Example:
    --------
    >>> import pandas as pd
    >>> data = {
    ...     'employee_id': [1, 2, 3, 4, 5],
    ...     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    ...     'department': ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance'],
    ...     'salary': [70000, 80000, 75000, 72000, 68000]
    ... }
    >>> employees = pd.DataFrame(data)
    >>> selectFirstRows(employees)
       employee_id     name   department  salary
    0            1    Alice           HR   70000
    1            2      Bob  Engineering   80000
    2            3  Charlie    Marketing   75000
    """
    # Use the head() method to return the first 3 rows
    # head(3) is equivalent to head(n=3)
    # If the DataFrame has fewer than 3 rows, all rows are returned
    return employees.head(3)


# ============================================================================
# DEMONSTRATION SECTION: Sample data and DataFrame creation
# ============================================================================

# Create sample employee data as a dictionary
# Each key is a column name, and each value is a list of data for that column
# This simulates a real-world scenario with 5 employees and their attributes
data = {
    'employee_id': [1, 2, 3, 4, 5],  # Unique employee identifiers
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],  # Employee names
    'department': ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance'],  # Department assignments
    'salary': [70000, 80000, 75000, 72000, 68000]  # Annual salaries
}

# Create a DataFrame from the sample employee data
# This converts the dictionary into a structured, tabular format
employees = pd.DataFrame(data)

# Display the DataFrame for reference
print("Full DataFrame:")
print(employees)
print()

# Call the function to extract and display the first 3 rows
print("First 3 rows of the employees DataFrame:")
result = selectFirstRows(employees)
print(result)

# Expected Output:
#    employee_id     name   department  salary
# 0            1    Alice           HR   70000
# 1            2      Bob  Engineering   80000
# 2            3  Charlie    Marketing   75000
