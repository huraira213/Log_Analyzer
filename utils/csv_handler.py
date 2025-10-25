import csv

file_name = "data/filtered_logs.csv"

def read_from_csv():
    """Read logs data from csv file"""
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"{file_name} not found. Returning empty list.")
        return []
    except Exception as e:
        print(f"Error reading from {file_name}: {e}")
        return []

def create_dict(results):
    logs = read_from_csv()
    log_id = len(logs) + 1
    for r in results:
        date, time, level, message = r.values()
        new_log = {
            'id': log_id,
            'date': date,
            'time': time,
            'level': level,
            'message': message
        }
        logs.append(new_log)
        log_id += 1  # increment for each new record
    save_filtered_logs_csv(logs)


def save_filtered_logs_csv(logs):
    """Save filtered logs to a CSV file."""
    try:
        with open(file_name, mode='w', newline='') as file:
            fieldnames = ["id", "date", "time", "level", "message"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for log in logs:
                writer.writerow(log)

        print(f"Saved to {file_name} successfully.")
    except Exception as e:
        print(f"Error saving to {file_name}: {e}")
