# Name: Stephan Jones
# Student ID: 500004652
# Date: 23rd October 2026
# Question: Q3 Parish Incident Summary - Part 1
# Collaborators: none
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
    
    if code in PARISH_CODES.split():
        return True
    return False

def is_valid_type(code: str) -> bool:
    """Return True if code is exactly one of the five incident type codes."""
    
    if code in TYPE_CODES.split():
        return True
    return False

def normalise_report(raw: str) -> str:
    """Return raw with leading/trailing whitespace removed, in upper case."""

    return raw.strip().upper()


def is_valid_report(report: str) -> bool:
    """Return True if a normalised report has the form PP-TTT-HH with valid parts."""

    if len(report) != REPORT_LENGTH:
        return False

    parts = report.split("-")
    if len(parts) != 3:
        return False

    parish_code, type_code, hour_code = parts
    if not is_valid_parish(parish_code):
        return False
    if not is_valid_type(type_code):
        return False
    if not (hour_code.isdigit() and 0 <= int(hour_code) <= MAX_HOUR):
        return False

    return True


def main() -> None:
    """Read reports until END and print the valid/invalid counts."""
    
    valid_count = 0
    invalid_count = 0

    while True:
        raw_report = input(REPORT_PROMPT)
        report = normalise_report(raw_report)

        if report == SENTINEL:
            break

        if is_valid_report(report):
            valid_count += 1
        else:
            invalid_count += 1

    print(f"Valid reports: {valid_count}")
    print(f"Invalid reports: {invalid_count}")



if __name__ == "__main__":
    main()
