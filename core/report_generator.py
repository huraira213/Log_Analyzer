# core/report_generator.py
import datetime
import json
from pathlib import Path

class ReportGenerator:
    def __init__(self, analyzer):
        self.analyzer = analyzer  # instance of LogAnalyzer

    def display_summary(self):
        summary = self.analyzer.get_summary()

        # print raw dictionary (quick debug)
        print("DEBUG: Summary dictionary:", summary)

        # safely access values
        print(f"Total entries: {summary.get('total_entries', 0)}")

        print("\nLevel counts:")
        for level, count in summary.get('level_counts', {}).items():
            print(f"  {level}: {count}")

        print("\nTop errors:")
        for err in summary.get('top_errors', []):
            print(f"  {err}")

    def generate_text_report(self, file_path):
        try:
            # Write a summary to a text file (report.txt)
            summary = self.analyzer.get_summary()
            top_errors = self.analyzer.get_top_errors()

            report_content = self._format_text_report(summary, top_errors)
            Path(file_path).write_text(report_content, encoding="utf-8")
            print(f" Report saved to {file_path}")
        except Exception as e:
            raise ValueError(f"Error generating report: {e}")

    def generate_json_summary(self, file_path):
        try:
            # Save counts and filtered logs to JSON
            summary_data = self.analyzer.get_summary()
            Path(file_path).write_text(json.dumps(summary_data, indent=4))
            print(f"JSON summary saved to {file_path}")
        except Exception as e:
            raise JsonError(f"Error saving JSON summary: {e}")

    def _format_text_report(self, summary, top_errors):
        """Private helper to format text report."""
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = []
        report.append("=" * 50)
        report.append("                LOG ANALYSIS REPORT")
        report.append("=" * 50)
        report.append(f"\n Report Generated: {now}")
        #report.append(f" Source Directory: {self.log_dir}")
        report.append("\n" + "-" * 50)
        report.append("SUMMARY")
        report.append("-" * 50)
        report.append(f"Total Log Entries: {summary['total_entries']}")
        for level, count in summary['level_counts'].items():
            report.append(f"{level:<8} : {count}")

        report.append("\n" + "-" * 50)
        report.append("TOP ERRORS (first 5)")
        report.append("-" * 50)
        for err in top_errors[:5]:
            report.append(str(err))

        report.append("\n" + "-" * 50)
        report.append("NOTES")
        report.append("-" * 50)
        report.append("Report generated automatically by Log Analyzer v2.")
        return "\n".join(report)