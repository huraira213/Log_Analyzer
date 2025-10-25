from collections import Counter

def analyze_logs(lines):
    """Analyze file line by line"""
    try:
        print(f"Total lines read: {len(lines)}")
        print("First few lines:")
        print("=" * 50)
        for line in lines[:5]:
            print(line)
        print("=" * 50)
    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
        return []

def parse_log_line(line):
    """Parse a single log line into structured data"""
    try:
        parts = line.split(" ", 3)
        if len(parts) < 4:
            return None

        date, time, level, message = parts
        return {
            "date": date,
            "time": time,
            "level": level,
            "message": message
        }

    except Exception as e:
        print(f"Error: {e}")
        return None


def count_log_levels(parsed_logs):
    """Count how many times each log level appears"""
    try:
        levels = [log["level"] for log in parsed_logs if "level" in log]
        counts = Counter(levels)
        print("=" * 50)
        print("\n--- Log Level Summary ---")
        for level, count in counts.items():
            print(f"{level}: {count}")
        print("=" * 50)
    except Exception as e:
        print(f"Error: {e}")

def filter_by_level(parsed_logs, level):
    """Filter logs by given level (INFO, ERROR, WARNING, etc.)"""
    try:
        results = [log for log in parsed_logs if log["level"].upper() == level.upper()]

        if not results:
            print(f"No logs found for level: {level}")
        else:
            print(f"\n--- Logs with level: {level.upper()} ---")
            for log in results:
                print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
            return results
    except Exception as e:
        print(f"Error: {e}")
