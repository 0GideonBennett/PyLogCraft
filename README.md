# PyLogCraft
This project contains two lightweight Python scripts designed to help system administrators or analysts quickly process log files.


## 📌 Features

### 1. Error Finder
- Prompts the user for a log file name and a keyword.
- Scans the log and returns all lines that contain the keyword (e.g., `ERROR`, `WARNING`, `CRITICAL`).
- Useful for quickly isolating meaningful entries during log analysis.

### 2. Log Combiner
- Prompts the user for two log files and creates a third file that combines them.
- Automatically adds a separator (`Next Log Start:`) between the two logs.
- Helpful when merging logs from different systems or timeframes.

## 🚀 Getting Started

### Prerequisites and Notes
- Python 3.x installed on your system
- You must have your input logs within your current directory before running

### Future Improvement (v2)
- Allow users to restart the script without relaunching
- Add timestamped entries in the combined file
- Add support for appending instead of overwriting
  

### Running the Script
1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python log-scripts.py

