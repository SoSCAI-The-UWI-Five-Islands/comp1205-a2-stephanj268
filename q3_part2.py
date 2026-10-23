# Name: <your full name>
# Student ID: <your ID>
# Date: <date you started>
# Question: Q3 Parish Incident Summary - Part 2
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Count incident reports for one parish by type, one record at a time."""

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


def report_parish(report: str) -> str:
    """Return the parish code of a valid report."""
    
    parts = report.split("-")
    return parts[0]


def report_type(report: str) -> str:
    """Return the incident type code of a valid report."""
   
    parts = report.split("-")
    return parts[1]


def report_hour(report: str) -> int:
    """Return the hour (0-23) of a valid report."""
   
    parts = report.split("-")
    return int(parts[2])


def most_common_type(thf: int, bur: int, asl: int, trf: int, van: int) -> str:
    """Return the type code with the highest count (ties: THF, BUR, ASL, TRF, VAN)."""

    if thf > bur and thf > asl and thf > trf and thf > van:
        return "THF"
    elif bur > asl and bur > trf and bur > van:
        return "BUR"
    elif asl > trf and asl > van:
        return "ASL"
    elif trf > van:
        return "TRF"
    else:
        return "VAN"


def read_parish_code() -> str:
    """Prompt until a valid parish code is typed; return it normalised."""

    while True:
        code = input("Parish code: ")
        normalised_code = normalise_report(code)
        if is_valid_parish(normalised_code):
            return normalised_code
        print("Invalid parish code.")
        print("Try again.")


def main() -> None:
    """Read reports until END and print the summary for the chosen parish."""
    
    parish_code = read_parish_code()
    parish_code = normalise_report(parish_code)

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
    print(f"THF: {thf}")
    print(f"BUR: {bur}")
    print(f"ASL: {asl}")
    print(f"TRF: {trf}")
    print(f"VAN: {van}")
    print(f"Most common type: {most_common_type(thf, bur, asl, trf, van)}")



if __name__ == "__main__":
    main()
