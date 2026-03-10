# Python Scripts Repository

A collection of well-documented, production-ready Python scripts designed for data processing, analysis, and system-level tasks. This repository contains practical solutions for common data manipulation and log analysis challenges.

## 📋 Overview

This repository serves as a reference for building efficient Python applications that handle:
- DataFrame operations and transformations
- Large-scale data processing
- Log file analysis and insights extraction
- Data structure manipulation with streaming approaches

All scripts are optimized for clarity, performance, and robustness, with comprehensive inline documentation and error handling.

---

## 🔧 Prerequisites

### Required
- **Python 3.7+** (Recommended: Python 3.9 or later)
- **pip** (Python package manager)

### Dependencies
Install the required Python packages using pip:

```bash
pip install pandas
```

### Recommended
- **Virtual Environment** (venv or conda) for isolated package management
  ```bash
  # Create a virtual environment
  python3 -m venv venv
  
  # Activate it
  source venv/bin/activate  # On macOS/Linux
  # or
  venv\Scripts\activate     # On Windows
  ```

---

## 📁 Repository Structure

```
python-scripts/
├── dataFrameSize.py          # DataFrame dimension calculator
├── dataframeFromList.py       # Convert 2D list to DataFrame
├── logAnalysis.py             # Apache log file analyzer
├── README.md                  # This file
└── <new_script>.py           # (Add new scripts here)
```

---

## 📚 Available Scripts

### 1. **dataFrameSize.py** - DataFrame Dimension Calculator

**Purpose:**  
Calculate and retrieve the dimensions (number of rows and columns) of a pandas DataFrame.

**Use Cases:**
- Quickly determine DataFrame structure
- Verify data loading success
- Check dataset size before processing

**Dependencies:**
- `pandas`
- `typing` (standard library)

**Usage:**
```python
import pandas as pd
from dataFrameSize import getDataframeSize

# Create a sample DataFrame
data = {
    'player_id': [846, 749, 155, 583],
    'name': ['Mason', 'Riley', 'Bob', 'Isabella'],
    'age': [21, 30, 28, 32],
    'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper']
}
players_df = pd.DataFrame(data)

# Get dimensions
size = getDataframeSize(players_df)
print(size)  # Output: [4, 4]
```

**Output Format:**
```
[number_of_rows, number_of_columns]
```

---

### 2. **dataframeFromList.py** - Convert 2D List to DataFrame

**Purpose:**  
Convert a 2D list of student data into a structured pandas DataFrame with meaningful column names.

**Use Cases:**
- Transform raw nested list data into DataFrames
- Standardize data import from custom sources
- Prepare data for analysis workflows

**Dependencies:**
- `pandas`
- `typing` (standard library)

**Usage:**
```python
from dataframeFromList import createDataframe

# Define student data as 2D list
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

# Create DataFrame
df = createDataframe(student_data)
print(df)
```

**Output:**
```
   student_id  age
0           1   15
1           2   11
2           3   11
3           4   20
```

---

### 3. **logAnalysis.py** - Apache Log File Analyzer

**Purpose:**  
Analyze large Apache-style access log files to identify the top 5 IP addresses that triggered 500 Internal Server Errors.

**Use Cases:**
- Identify problematic clients in production environments
- Debug server error patterns
- Monitor security and performance issues
- Handle massive log files (20GB+) with minimal memory overhead

**Key Features:**
- ✅ Streams files line-by-line (memory efficient)
- ✅ Handles malformed log entries gracefully
- ✅ Uses regex for efficient parsing
- ✅ Returns top 5 IPs with error counts
- ✅ No heavy dependencies (only standard library)

**Dependencies:**
- `re` (standard library - regex)
- `collections` (standard library - Counter, defaultdict)

**Log Format:**
```
192.168.1.1 - - [09/Mar/2026:14:00:01 +0000] "GET /api/v1/checkout HTTP/1.1" 500 1234
```

Where:
- `192.168.1.1` = Client IP address
- `[timestamp]` = Request timestamp
- `GET /api/v1/checkout HTTP/1.1` = HTTP request
- `500` = HTTP status code (the error we're tracking)
- `1234` = Response size in bytes

**Usage:**
```python
from logAnalysis import get_top_error_ips

# Analyze production access log
get_top_error_ips('production_access.log')
```

**Output Example:**
```
192.168.1.1: 245
192.168.1.2: 189
192.168.1.3: 156
10.0.0.5: 98
10.0.0.7: 87
```

---

## 🚀 Getting Started

### 1. Clone or Download the Repository
```bash
git clone https://github.com/yourusername/python-scripts.git
cd python-scripts
```

### 2. Set Up Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install pandas
```

### 4. Run a Script
```bash
# Run DataFrame size calculator
python3 dataFrameSize.py

# Run DataFrame creation
python3 dataframeFromList.py

# Run log analysis (requires production_access.log file)
python3 logAnalysis.py
```

---

## 📖 Script Documentation

Each script includes:
- ✅ **Module-level docstring** - Overall purpose and functionality
- ✅ **Function docstrings** - Parameter descriptions, return values, and examples
- ✅ **Inline comments** - Detailed explanations of logic and algorithms
- ✅ **Example usage** - Practical demonstrations with sample data
- ✅ **Error handling** - Graceful handling of edge cases

---

## 🔄 Adding New Scripts

When adding a new script to this repository:

1. **Create the script** with comprehensive documentation
2. **Update this README.md** with:
   - A new section under **Available Scripts**
   - Purpose and use cases
   - Required dependencies
   - Usage example with code and expected output
   - Any special considerations

3. **Use this template for documentation:**
   ```markdown
   ### N. **script_name.py** - Brief Description
   
   **Purpose:**  
   One-line description of what the script does.
   
   **Use Cases:**
   - Use case 1
   - Use case 2
   
   **Dependencies:**
   - dependency1
   - dependency2
   
   **Usage:**
   ```python
   [Example code]
   ```
   
   **Output:**
   [Expected output]
   ```

---

## 🛠️ Troubleshooting

### ModuleNotFoundError: No module named 'pandas'
```bash
# Install pandas
pip install pandas
```

### FileNotFoundError in logAnalysis.py
```bash
# Ensure the log file exists in the correct directory
# Update the file path in the function call:
get_top_error_ips('/path/to/production_access.log')
```

### Python version issues
```bash
# Check your Python version
python3 --version

# Ensure you're using Python 3.7 or later
```

---

## 📝 License

This repository is available for educational and commercial use.

---

## 💡 Best Practices

- Always use virtual environments for project isolation
- Review docstrings before using a function
- Handle exceptions appropriately in production code
- Test scripts with sample data before using with real data
- For large files (like 20GB logs), use streaming/iterator approaches

---

## ✨ Features Across Scripts

| Feature | dataFrameSize.py | dataframeFromList.py | logAnalysis.py |
|---------|------------------|----------------------|----------------|
| Memory Efficient | ✅ | ✅ | ✅ (Streaming) |
| Error Handling | ✅ | ✅ | ✅ |
| Type Hints | ✅ | ✅ | ✅ |
| Documented | ✅ | ✅ | ✅ |
| Pandas Required | ✅ | ✅ | ❌ |
| Scalable | ✅ | ✅ | ✅ (20GB+) |

---

## 📬 Feedback

For questions or improvements, feel free to open an issue or submit a pull request.

**Last Updated:** March 9, 2026