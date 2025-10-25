import json
import csv
from core.analyzer import (filter_by_level)
from utils.csv_handler import (create_dict, save_filtered_logs_csv)



def read_file_log(file_path):
    """"Read file and return lines as a list"""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
        return []

def save_logs_json(parsed_logs, output_path):
    """Save logs to a json file"""
    try:
        with open(output_path, 'w') as file:
            json.dump(parsed_logs, file, indent=4)

    except Exception as e:
        print(f"Error: {e}")

def search_log(parsed_logs):
    """search logs"""
    print("-- Filter Logs --")
    print("=" * 50)
    try:
        level = input("Enter log level to search for: ").strip().upper()
        results = filter_by_level(parsed_logs, level)
        if not results:
            print("No logs found for the given level.")
            return
        # ask to store log in csv file
        choice = input("Do you want to store the results? (y/n): ").strip().lower()
        if choice == "y":
            create_dict(results)
        elif choice == "n":
            print("Exiting...")
            return
        else:
            print("Invalid input. Exiting...")

    except Exception as e:
        print(f"Error: {e}")


