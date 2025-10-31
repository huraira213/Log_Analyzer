# utils/log_reader.py
import os
from pathlib import Path
from utils.file_utils import ensure_directory, list_log_files, get_full_path

class LogReader:
    """Handles reading and listing log files from a given directory."""

    def __init__(self, log_dir: str):
        """Initialize the LogReader with a directory path."""
        self.log_dir = Path(log_dir)
        ensure_directory(self.log_dir)

    def list_logs(self):
        """Return a list of available .log files in the directory."""
        logs = list_log_files(self.log_dir)
        if not logs:
            print(f"No .log files found in {self.log_dir}")
        return logs

    def read_file(self, file_name: str):
        """Read a given log file and return its lines as a list."""
        try:
            path = get_full_path(self.log_dir, file_name)

            if not path.exists():
                raise FileNotFoundError(f"File '{file_name}' not found in {self.log_dir}")

            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                lines = [line.strip() for line in file if line.strip()]

            return lines

        except Exception as e:
            print(f"Error reading file: {e}")
