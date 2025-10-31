#  Log Analyzer (OOP-Based Mini Project)

A simple **Object-Oriented Log Analyzer** written in Python that reads log files, parses structured data, analyzes patterns, and generates both **text** and **JSON** reports.

---

##  Project Overview

This mini project demonstrates clean software design using **OOP principles**, including separation of concerns, modularity, and reusability.

It can:

* Parse logs into structured objects (`LogEntry`).
* Count occurrences by log level (INFO, WARNING, ERROR).
* Identify top frequent errors.
* Export readable summaries to **text** or **JSON** reports.

---

##  Features

| Feature                    | Description                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| **Log Parsing**            | Reads logs line by line and converts each into a structured `LogEntry` object.                |
| **Data Analysis**          | Counts log levels and extracts top errors using `LogAnalyzer`.                                |
| **Report Generation**      | Creates human-readable `.txt` and machine-readable `.json` summaries using `ReportGenerator`. |
| **Error Handling**         | Handles missing files, malformed logs, and unexpected data gracefully.                        |
| **Object-Oriented Design** | Clean modular architecture with dedicated classes for each responsibility.                    |

---

##  Project Structure

```
log_analyzer_oop/
│
├── main.py                      # Entry point (User Interface)
├── core/
│   ├── log_entry.py             # LogEntry class (represents a single log line)
│   ├── log_analyzer.py          # LogAnalyzer class (analysis logic)
│   └── report_generator.py      # ReportGenerator class (output generation)
│
├── data/
│   └── logs.txt                 # Sample log file
│
└── reports/
    ├── report.txt               # Human-readable text report
    └── report.json              # JSON summary report
```

---

##  How It Works

1. **Load Logs**

   * The program reads all `.txt` log files from the `/data` directory.
   * Each line is parsed into a `LogEntry` object.

2. **Analyze Logs**

   * `LogAnalyzer` counts how many `INFO`, `WARNING`, and `ERROR` logs exist.
   * It identifies the most frequent error messages.

3. **Generate Reports**

   * Choose between two output types:

     * **Text report** → easy to read.
     * **JSON summary** → easy to process programmatically.

---

##  Example Output

###  Text Report

```
==================================================
                LOG ANALYSIS REPORT
==================================================

 Report Generated: 2025-10-31 18:56:27

--------------------------------------------------
SUMMARY
--------------------------------------------------
Total Log Entries: 10
INFO     : 5
WARNING  : 3
ERROR    : 2

--------------------------------------------------
TOP ERRORS (first 5)
--------------------------------------------------
[ERROR] 2025-10-27 13:10:07 - Unable to connect to database
[ERROR] 2025-10-27 13:10:07 - Unable to connect to database

--------------------------------------------------
NOTES
--------------------------------------------------
Report generated automatically by Log Analyzer v2.
```

###  JSON Report

```json
{
  "total_entries": 10,
  "level_counts": {
    "INFO": 5,
    "WARNING": 3,
    "ERROR": 2
  },
  "top_errors": [
    {
      "date": "2025-10-27",
      "time": "13:10:07",
      "level": "ERROR",
      "message": "Unable to connect to database"
    }
  ]
}
```

---

##  How to Run

1. Clone or download this repository.
2. Place your `.log` or `.txt` files in the `data/` folder.
3. Run the main file:

```bash
python main.py
```

4. Follow the menu options to:

   * View logs
   * Filter by level
   * Generate reports

---

##  Concepts Practiced

* Object-Oriented Design (Encapsulation, Composition)
* File Handling and Parsing
* Data Aggregation and Reporting
* Exception Handling
* JSON and Text File I/O
* Modular Software Design

---

##  Author

**Huraira Khurshid**
 Python Developer & Intern at SKAI Worldwide
 Completed: October 2025
 Goal: Building clean, modular, and maintainable Python software.

---

##  License

This project is open-source and available for educational use.
