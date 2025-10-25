from utils.file_handler import (read_file_log, save_logs_json, search_log)
from core.analyzer import (analyze_logs, parse_log_line, count_log_levels)


def user_interface(lines, parsed_logs):
    """helper for main menu"""
    try:
        print("-- Welcome to the Log Analyzer --")
        print("=" * 50)
        file_path = "data/sample.log"
        while True:
            print("1. View Log Summary ")
            print("2. Search Logs by Level (INFO, ERROR, etc.)")
            print("3. View Log Entries")
            print("4. Export to json")
            print("5. Filter Logs and save to csv")
            print("7. Exit")
            choice = input("What would you like to do?: ")

            if choice == "1":
                count_log_levels(parsed_logs)
            elif choice == "2":
                searches(parsed_logs)
            elif choice == "3":
                analyze_logs(lines)
            elif choice == "4":
                save_logs_json(parsed_logs, "data/parse_log.json")
            elif choice == "5":
                search_log(parsed_logs)
            elif choice == "7":
                print("Exiting...")
                break

    except Exception as e:
        print(f"Error: {e}")

def main_menu():
    """handle users interface"""
    file_path = "data/sample.log"
    lines = read_file_log(file_path)

    if not lines:
        print("File not found.")
        return

    # Parse all logs into a list of dicts
    parsed_logs = []
    for line in lines:
        parsed = parse_log_line(line)
        if parsed:
            parsed_logs.append(parsed)
    user_interface(lines, parsed_logs)


