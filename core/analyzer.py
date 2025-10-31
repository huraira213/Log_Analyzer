# analyzer.py
from collections import Counter

class LogAnalyzer:
    """Main class for parsing and analyzing log files."""

    def __init__(self):
        self.logs = []  # List of LogEntry objects

    # 1. ---------------- Parse a single log line ----------------
    def parse_line(self, line):
        """Parse a single line into a LogEntry object."""
        try:
            parts = line.split(" ", 3)
            if len(parts) < 4:
                return None
            date, time, level, message = parts
            return LogEntry(date, time, level.upper(), message)
        except Exception as e:
            print(f"[Error] Failed to parse line: {e}")
            return None

    # 2. ---------------- Parse entire log file ----------------
    def parse_file(self, file_path):
        """Read and parse a log file."""
        self.logs = []  # clear old logs
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    entry = self.parse_line(line.strip())
                    if entry:
                        self.logs.append(entry)
            print(f" Loaded {len(self.logs)} log entries from {file_path}")
        except Exception as e:
            print(f"[Error] Failed to load log file: {e}")

    # 3. ---------------- Filter logs ----------------
    def filter_by_level(self, level):
        """Return all logs with the given level."""
        return [log for log in self.logs if log.level == level.upper()]

    # 4. ---------------- Count log levels ----------------
    def count_levels(self):
        """Count how many times each log level appears."""
        level_counts = Counter(log.level for log in self.logs)
        return dict(level_counts)

    # 5. ---------------- Search logs ----------------
    def search(self, keyword):
        """Search for a keyword in log messages."""
        keyword = keyword.lower()
        return [log for log in self.logs if keyword in log.message.lower()]

    # 6. ---------------- Show sample lines ----------------
    def preview(self, n=5):
        """Preview the first n log entries."""
        for log in self.logs[:n]:
            print(log)

    def get_top_errors(self, limit=5):
        """Return the first N ERROR log entries."""
        try:
            errors = [log for log in self.logs if log.level == "ERROR"]
            return errors[:limit]
        except Exception as e:
            print(f"Error retrieving top errors: {e}")
            return []

    def get_summary(self, limit=5):
        """Return a structured summary of the log analysis."""
        try:
            total = len(self.logs)
            level_counts = self.count_levels()
            top_errors = [e.to_dict() for e in self.get_top_errors(limit)]

            return {
                "total_entries": total,
                "level_counts": level_counts,
                "top_errors": top_errors,
            }
        except Exception as e:
            print(f"Error generating summary: {e}")
            return {}


class LogEntry:
    """Represents one structured log entry."""

    def __init__(self, date, time, level, message):
        self.date = date
        self.time = time
        self.level = level
        self.message = message

    def __repr__(self):
        return f"[{self.level}] {self.date} {self.time} - {self.message}"

    def to_dict(self):
        return {
            "date": self.date,
            "time": self.time,
            "level": self.level,
            "message": self.message
        }

