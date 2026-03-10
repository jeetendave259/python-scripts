"""
Log Analysis at Scale Module

This module provides functionality to analyze large Apache-style access log files
and identify the most problematic IP addresses based on HTTP 500 Internal Server Errors.

PROBLEM STATEMENT:
You have a standard Apache-style access log file named production_access.log. 
Each line follows this format:
192.168.1.1 - - [09/Mar/2026:14:00:01 +0000] "GET /api/v1/checkout HTTP/1.1" 500 1234

Where:
- 192.168.1.1: Client IP address
- - -: Remote user and authentication (typically empty)
- [09/Mar/2026:14:00:01 +0000]: Timestamp of the request
- "GET /api/v1/checkout HTTP/1.1": HTTP request (method, path, protocol)
- 500: HTTP status code (the error we're interested in)
- 1234: Response size in bytes

TASK:
Reads the file efficiently and identifies the top 5 IP addresses that triggered 
a 500 Internal Server Error, then outputs the IPs and their respective counts.

CONSTRAINTS:
1. Cannot use heavy libraries like Pandas (demonstrates proficiency with standard 
   libraries like re, collections, and io)
2. Must handle malformed lines without crashing
3. File is assumed to be 20GB and cannot fit entirely in RAM, so streaming is required

APPROACH:
- Stream the file line-by-line to minimize memory usage
- Use regex to parse each log entry efficiently
- Use collections.defaultdict for counting with automatic 0 initialization
- Use collections.Counter.most_common() to get top 5 IPs quickly
"""

import re                  # For efficient pattern matching and log line parsing
import collections        # For defaultdict and Counter data structures


def get_top_error_ips(filename):
    """
    Reads an Apache-style access log file and identifies the top 5 IP addresses 
    that triggered a 500 Internal Server Error.

    This function is designed to handle very large log files (20GB+) by streaming
    the file line-by-line without loading the entire file into memory. It uses
    regex to extract relevant information and efficient data structures for 
    counting and sorting.

    Parameters:
    -----------
    filename : str
        Path to the Apache-style access log file.
        Expected format: IP - - [timestamp] "HTTP_REQUEST" STATUS_CODE RESPONSE_SIZE
        Example: 192.168.1.1 - - [09/Mar/2026:14:00:01 +0000] "GET /api/v1/checkout HTTP/1.1" 500 1234

    Returns:
    --------
    None
        Prints the top 5 IP addresses and their respective counts of 500 errors
        to standard output in the format: IP: count

    Raises:
    -------
    FileNotFoundError: If the specified file does not exist
    Exception: Generic exception handling for unexpected errors during file reading
    
    Example:
    --------
    >>> get_top_error_ips('production_access.log')
    192.168.1.1: 245
    192.168.1.2: 189
    192.168.1.3: 156
    10.0.0.5: 98
    10.0.0.7: 87
    """
    
    # Use defaultdict with int as the default factory to count IP occurrences
    # This automatically initializes missing keys with 0, eliminating need for 
    # key existence checks before incrementing
    ip_counts = collections.defaultdict(int)
    
    try:
        # Open file and iterate line-by-line (streaming approach)
        # This is critical for memory efficiency with large files
        # Instead of loading all 20GB into memory at once, only one line is in memory
        with open(filename, 'r') as f:
            for line in f:
                # Define the regex pattern to extract IP and HTTP status code
                # Pattern explanation:
                # ^(\S+)           - Captures the IP address (first non-whitespace group at line start)
                # .*?              - Matches any characters (non-greedy) for the user/auth section
                # "\S+ .*?"        - Matches the HTTP request line (method and path)
                # (\d{3})          - Captures the 3-digit HTTP status code
                # Pattern ensures we don't accidentally match wrong 3-digit numbers later in the line
                log_pattern = re.compile(r'^(\S+) .*? "\S+ .*?" (\d{3}) ')
                
                # Attempt to match the pattern against the current line
                # If the line is malformed and doesn't match, skip it gracefully
                match = log_pattern.match(line)
                if not match:
                    # Skip malformed lines silently (no crash, no loud error)
                    continue
                
                # Extract the IP address from the first capturing group
                ip = match.group(1)
                
                # Extract the HTTP status code from the second capturing group
                status_code = match.group(2)
                
                # Filter for only 500 Internal Server Errors
                # Only increment the counter if status code is exactly "500"
                if status_code == "500":
                    ip_counts[ip] += 1
    
    except FileNotFoundError:
        # Handle case where the log file doesn't exist
        print("File not found.")
        return
    
    except Exception as e:
        # Catch any unexpected errors during file processing
        # This could include permission errors, encoding errors, etc.
        print(f"An unexpected error occurred: {e}")
        return
    
    # Convert defaultdict to Counter for efficient sorting
    # Counter.most_common(5) returns the 5 most frequent IPs as a list of tuples
    # This is more efficient than manually sorting the entire dictionary
    top_5 = collections.Counter(ip_counts).most_common(5)
    
    # Print the results: each IP and its count of 500 errors
    # Format: IP_ADDRESS: ERROR_COUNT
    for ip, count in top_5:
        print(f"{ip}: {count}")


# ============================================================================
# USAGE INSTRUCTIONS
# ============================================================================
# To run this script and analyze a log file:
# >>> get_top_error_ips('production_access.log')
#
# This will print the top 5 IP addresses with the most 500 errors
# Example output:
# 192.168.1.1: 245
# 192.168.1.2: 189
# 192.168.1.3: 156
# 10.0.0.5: 98
# 10.0.0.7: 87