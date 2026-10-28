# Name: Stephan Jones
# Student ID: 500004652
# Date: 23rd October 2026
# Question: Q3 Parish Incident Summary - Part 3
# Collaborators: none
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

    if thf >= bur and thf >= asl and thf >= trf and thf >= van:
        return "THF"
    elif bur >= asl and bur >= trf and bur >= van:
        return "BUR"
    elif asl >= trf and asl >= van:
        return "ASL"
    elif trf >= van:
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


def format_hour(hour: int) -> str:
    """Return hour as two digits, or N/A when no hour was recorded."""
    
    if hour == -1:
        return "N/A"
    return f"{hour:02d}"


def main() -> None:
    """Read reports until END and print the summary for the chosen parish."""

    parish_code = read_parish_code()
    parish_code = normalise_report(parish_code)
    
    valid_count = 0
    invalid_count = 0
    parish_total = 0
    thf = 0
    bur = 0
    asl = 0
    trf = 0
    van = 0
    
    while True:
        raw_report = input(REPORT_PROMPT)
        report = normalise_report(raw_report)
    
    
        if report == SENTINEL:
            break
    
        if is_valid_report(report):
            valid_count += 1
            if report_parish(report) == parish_code:
                parish_total += 1
            report_type_code = report_type(report)
            if report_type_code == "THF":
                thf += 1
            elif report_type_code == "BUR":
                bur += 1
            elif report_type_code == "ASL":
                asl += 1
            elif report_type_code == "TRF":
                trf += 1
            elif report_type_code == "VAN":
                van += 1
        else:
            invalid_count += 1
    
    print(f"Valid reports: {valid_count}")
    print(f"Invalid reports: {invalid_count}")
    
    print(f"THF: {thf}")
    print(f"BUR: {bur}")
    print(f"ASL: {asl}")
    print(f"TRF: {trf}")
    print(f"VAN: {van}")
    
    print(f"Parish {parish_code} total: {parish_total}")
    if parish_total > 0:
        most_common = most_common_type(thf, bur, asl, trf, van)
        print(f"Most common type: {most_common}")

    earliest_hour = NO_HOUR
    latest_hour = NO_HOUR
    longest_streak = 0

    if earliest_hour != NO_HOUR:
        earliest_hour = format_hour(earliest_hour)
    if latest_hour != NO_HOUR:
        latest_hour = format_hour(latest_hour)

    print(f"Earliest hour: {earliest_hour}")
    print(f"Latest hour: {latest_hour}")

    
    print(f"Longest streak: {longest_streak}")

     

    


if __name__ == "__main__":
    main()
