#file_utils.py
from pathlib import Path

def get_logs_path() -> Path:
    return Path("data/logs").resolve()

def ensure_directory(path: Path) -> None:
    """Ensure the directory exists. Create if missing."""
    path.mkdir(parents=True, exist_ok=True)

def get_full_path(*parts: str) -> Path:
    """Safely join paths and return a Path object."""
    return Path(*parts).resolve()

def list_log_files(log_folder: Path) -> list[str]:
    """Return a list of all .log file names in the given folder."""
    return [f.name for f in log_folder.glob("*.log")]
