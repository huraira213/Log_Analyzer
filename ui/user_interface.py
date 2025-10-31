# ui/user_interface.py
from utils.file_utils import get_logs_path
from core.log_reader import LogReader
from core.analyzer import LogAnalyzer
from core.report_generator import ReportGenerator  # upcoming module

class UserInterface:
    def __init__(self):
        self.log_dir = get_logs_path()
        self.reader = LogReader(self.log_dir)
        self.analyzer = LogAnalyzer()
        self.reporter = ReportGenerator(self.analyzer)

    def display_menu(self):
        print("\n=== LOG ANALYZER MENU ===")
        print("=" *30)
        print("1. List available logs")
        print("2. Load and parse a log file")
        print("3. Filter logs by level")
        print("4. Count log levels")
        print("5. Preview first few logs")
        print("6. Generate report (text/json)")
        print("7. Exit")

    def run(self):
        try:
            while True:
                self.display_menu()
                choice = input("Enter choice (1-7): ").strip()

                if choice == "1":
                    self.list_logs()
                elif choice == "2":
                    self.load_log()
                elif choice == "3":
                    self.filter_logs()
                elif choice == "4":
                    self.count_levels()
                elif choice == "5":
                    self.preview_logs()
                elif choice == "6":
                    self.generate_report()
                elif choice == "7":
                    print("Exiting... Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # --- Menu Actions ---
    def list_logs(self):
        logs = self.reader.list_logs()
        print("\n  Available log files:")
        print("-" * 30)
        for i, f in enumerate(logs, 1):
            print(f"{i}. {f}")
        print("-" * 30)

    def load_log(self):
        logs = self.reader.list_logs()
        if not logs:
            print("No logs found.")
            print("-" * 30)
            return
        self.list_logs()
        choice = input("Enter file number: ").strip()
        print("-" * 30)
        try:
            index = int(choice) - 1
            lines = self.reader.read_file(logs[index])
            for line in lines:
                entry = self.analyzer.parse_line(line)
                if entry:
                    self.analyzer.logs.append(entry)
            print(f"Loaded {len(self.analyzer.logs)} logs.")
            print("-" * 30)
            self.reporter.analyzer = self.analyzer
        except (ValueError, IndexError):
            print("Invalid selection.")

    def filter_logs(self):
        level = input("Enter log level (INFO, WARNING, ERROR): ").strip().upper()
        print("-" * 30)
        results = self.analyzer.filter_by_level(level)
        print(f"\nFound {len(results)} entries with level {level}:")
        for log in results:
            print(log)
        print("-" * 30)

    def count_levels(self):
        counts = self.analyzer.count_levels()
        print("-" * 30)
        for level, count in counts.items():
            print(f"{level}: {count}")
        print("-" * 30)

    def preview_logs(self):
        print("-" * 30)
        n = int(input("How many entries to preview? ").strip())
        self.analyzer.preview(n)
        print("-" * 30)

    def generate_report(self):
        print("\n1. Text report\n2. JSON summary")
        choice = input("Select report type: ").strip()
        if choice == "1":
            self.reporter.generate_text_report("data/output/report.txt")
        elif choice == "2":
            self.reporter.generate_json_summary("data/output/summary.json")
        else:
            print("Invalid choice.")
