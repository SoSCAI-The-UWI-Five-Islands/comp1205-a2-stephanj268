# Name: <your full name>
# Student ID: <your ID>
# Date: <date you started>
# Question: Q3 Parish Incident Summary - Part 1
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Count valid and invalid coded incident reports until the END sentinel."""

PARISH_CODES = "SJ SG SP SH SL SM BA"
TYPE_CODES = "THF BUR ASL TRF VAN"
PARISH_LENGTH = 2
TYPE_LENGTH = 3
REPORT_LENGTH = 9
MAX_HOUR = 23
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


def main() -> None:
    """Read reports until END and print the valid/invalid counts."""
    # TODO: replace 'pass' with your code.
    pass


if __name__ == "__main__":
    main()
