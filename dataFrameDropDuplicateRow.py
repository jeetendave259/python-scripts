# DataFrame customers
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | customer_id | int    |
# | name        | object |
# | email       | object |
# +-------------+--------+
# There are some duplicate rows in the DataFrame based on the email column.

# Write a solution to remove these duplicate rows and keep only the first occurrence.

# The result format is in the following example.

 

# Example 1:
# Input:
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 5           | Finn    | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+
# Output:  
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+
# Explanation:
# Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the DataFrame based on the 'email' column, keeping only the first occurrence.
    
    This function uses pandas' drop_duplicates() method to efficiently remove duplicate entries in the DataFrame
    based on the specified column. In this case, it identifies duplicates in the 'email' column and retains only
    the first occurrence of each unique email address.
    
    Parameters:
    -----------
    customers : pd.DataFrame
        A pandas DataFrame containing customer information with columns:
        - customer_id: Unique identifier for each customer (int)
        - name: Customer name (str/object)
        - email: Customer email address (str/object)
    
    Returns:
    --------
    pd.DataFrame
        A new DataFrame with duplicate rows removed based on the 'email' column, keeping only the first occurrence.
        The structure and column names are preserved.
        
        Example output:
           customer_id     name               email
        0            1     Ella
        1            2     David
        2            3     Zachary
        3            4     Alice
        5            6     Violet
    Example:
    --------
    >>> data = {
    ...     'customer_id': [1, 2, 3, 4,
    ...                     5, 6],
    ...     'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    ...     'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
    ... }
    >>> customers = pd.DataFrame(data)
    >>> dropDuplicateEmails(customers)
       customer_id     name               email
    0            1     Ella
    1            2     David
    2            3     Zachary
    3            4     Alice
    5            6     Violet
    """
    # Use the drop_duplicates() method to remove duplicate rows based on the 'email' column
    # keep='first' ensures that only the first occurrence of each duplicate is retained
    return customers.drop_duplicates(subset='email', keep='first')

# ============================================================================
# DEMONSTRATION SECTION: Sample data and DataFrame creation
# ============================================================================


if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'customer_id': [1, 2, 3, 4, 5, 6],
        'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
        'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
    }
    customers = pd.DataFrame(data)
    result = dropDuplicateEmails(customers)
    print(result)