# Automated Log Analysis Tool (log_analysis.py)
This Python script, located within the `IT_Automated_Tools` suite, is designed to analyze a system log file (e.g., `syslog.log`). It processes the log to generate two key reports, which are then saved as CSV files for analysis:

* **Error Message Counts:** A report counting the total occurrences of each unique **error message**, sorted by frequency (highest first).
* **User Statistics:** A summary of **INFO** and **ERROR** log entries encountered for each user, sorted alphabetically by username.

---

## 🚀 Usage

The script is executed using `python3` and requires the log file path as a command-line argument. If no argument is provided, the script defaults to using a file named `./syslog.log` in the current directory.

### Command Line Execution

Execute the script by providing the path to your log file:

```bash
# Execute directly from this directory
python3 log_analysis.py /path/to/your/system.log
```

## 🛠️ Design & Engineering Decisions

These points highlight the quality and robustness of the implementation.
	
Feature 	Engineering Principle Demonstrated 	
Defensive Coding 	Implements a try/except pattern during file writing to ensure robust error handling.
Modularity The scripts use professional entry points (if __name__ == "__main__": and #!/bin/bash with argument validation) for easy integration and testing.
Clarity	Utilizes type hinting and clear variable names for improved code readability and maintainability.

## 💡 Future Improvements

Configurable Output Directory: Allow the user to specify the output directory for the CSV files via a command-line flag (e.g., using Python's argparse module).
Log Format Flexibility: Parameterize the log file regex pattern to allow the utility to be easily adapted to different log formats beyond the current "ticky" pattern.
