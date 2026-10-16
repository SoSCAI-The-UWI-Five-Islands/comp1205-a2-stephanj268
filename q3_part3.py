# Name: <your full name>
# Student ID: <your ID>
# Date: <date you started>
# Question: Q3 Parish Incident Summary - Part 3
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Summarise coded incident reports for one parish, one record at a time."""

PARISH_CODES = "SJ SG SP SH SL SM BA"
TYPE_CODES = "THF BUR ASL TRF VAN"
PARISH_LENGTH = 2
TYPE_LENGTH = 3
REPORT_LENGTH = 9
MAX_HOUR = 23
NO_HOUR = -1
SENTINEL = "END"
REPORT_PROMPT = "Report (END to finish): "


def is_valid_parish(code: str) -> bool:
    """Return True if code is exactly one of the seven parish codes."""
    # TODO: replace 'pass' with your code.
    pass


def is_valid_type(code: str) -> bool:
    """Return True if code is exactly one of the five incident type codes."""
    # TODO: replace 'pass' with your code.
    pass


def normalise_report(raw: str) -> str:
    """Return raw with leading/trailing whitespace removed, in upper case."""
    # TODO: replace 'pass' with your code.
    pass


def is_valid_report(report: str) -> bool:
    """Return True if a normalised report has the form PP-TTT-HH with valid parts."""
    # TODO: replace 'pass' with your code.
    pass


def report_parish(report: str) -> str:
    """Return the parish code of a valid report."""
    # TODO: replace 'pass' with your code.
    pass


def report_type(report: str) -> str:
    """Return the incident type code of a valid report."""
    # TODO: replace 'pass' with your code.
    pass


def report_hour(report: str) -> int:
    """Return the hour (0-23) of a valid report."""
    # TODO: replace 'pass' with your code.
    pass


def most_common_type(thf: int, bur: int, asl: int, trf: int, van: int) -> str:
    """Return the type code with the highest count (ties: THF, BUR, ASL, TRF, VAN)."""
    # TODO: replace 'pass' with your code.
    pass


def read_parish_code() -> str:
    """Prompt until a valid parish code is typed; return it normalised."""
    # TODO: replace 'pass' with your code.
    pass


def format_hour(hour: int) -> str:
    """Return hour as two digits, or N/A when no hour was recorded."""
    # TODO: replace 'pass' with your code.
    pass


def main() -> None:
    """Read reports until END and print the summary for the chosen parish."""
    # TODO: replace 'pass' with your code.
    pass


if __name__ == "__main__":
    main()
