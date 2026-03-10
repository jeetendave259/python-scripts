"""
DataFrame Size Calculator Module

This module provides functionality to calculate and retrieve the dimensions (number of rows 
and columns) of a pandas DataFrame. It's particularly useful for quickly determining the 
structure and size of large datasets.

The module demonstrates:
1. Using pandas DataFrame.shape attribute to get dimensions
2. Type hinting with Python's typing module for better code clarity
3. Practical example with sample player data

Expected DataFrame Structure (players):
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| team        | object |
+-------------+--------+
"""

from typing import List  # Importing List for type hinting
import pandas as pd      # Importing pandas for DataFrame operations and data manipulation

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    """
    Calculate and return the dimensions of a pandas DataFrame.
    
    This function determines the number of rows and columns in a given DataFrame
    using the shape attribute, which is an efficient way to get DataFrame dimensions.
    
    Parameters:
    -----------
    players : pd.DataFrame
        A pandas DataFrame containing player information. Expected to have columns like
        player_id, name, age, position, and team.
    
    Returns:
    --------
    List[int]
        A list containing two integers: [number_of_rows, number_of_columns]
        Example: [10, 5] means 10 rows and 5 columns
    
    Example:
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    >>> getDataframeSize(df)
    [2, 2]
    """
    
    # Extract dimensions using the shape attribute
    # shape returns a tuple: (number_of_rows, number_of_columns)
    # This is more efficient than using len() for rows and df.columns for columns
    num_rows, num_columns = players.shape
    
    # Display the size information for verification and debugging purposes
    print(f"Number of rows: {num_rows}, Number of columns: {num_columns}")
    print(f"DataFrame size: [{num_rows}, {num_columns}]")
    print(f"DataFrame size as list: {[num_rows, num_columns]}")
    
    # Return the dimensions as a list in the format [rows, columns]
    return [num_rows, num_columns]


# ============================================================================
# DEMONSTRATION SECTION: Sample data and DataFrame creation
# ============================================================================

# Create sample data dictionary representing player information
# Each key is a column name, and each value is a list of data for that column
# This simulates a real-world scenario with 10 players and their attributes
data = {
    'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],  # Unique player identifiers
    'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],  # Player names
    'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],  # Player ages (ranging from 18 to 36)
    'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],  # Playing positions
    'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']  # Club teams
}

# Display the raw sample data dictionary
print("Data:")  # Header label
print(data)  # Print the dictionary for verification

# Create a DataFrame from the sample data dictionary
# This converts the dictionary into a structured tabular format that pandas can work with
# Rows represent individual players, columns represent different attributes
players_df = pd.DataFrame(data)

# Display the formatted DataFrame
print("DataFrame:")  # Header label for clarity
print(players_df)  # Print the DataFrame in a formatted table structure

# Call the function to calculate and display the DataFrame dimensions
size = getDataframeSize(players_df)

# Display the calculated size result
print("Size:")  # Header label
print(size)  # Output: [10, 5] - meaning 10 rows and 5 columns
