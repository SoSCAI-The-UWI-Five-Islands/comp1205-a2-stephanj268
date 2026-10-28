# Name: Stephan Javorn Jones
# Student ID: 500004652
# Date: 19th October 2026
# Question: Q1 Checkpoint Plate Reader - Part 3
# Collaborators: none
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Normalise and validate a licence plate, then match it against a watch-list pattern."""



CATEGORY_LETTERS = "PTHRBG"
BARBUDA_MARKER = "X"
MAX_LETTERS = 2
MIN_DIGITS = 1
MAX_DIGITS = 4
ANY_CHAR = "?"
ANY_DIGIT = "#"
ANY_LETTER = "@"


def is_letter(ch: str) -> bool:
    """Return True if ch is exactly one uppercase letter from A to Z.

    Optional helper: you may delete it or write your own. Not unit-tested.
    """
    
    if len(ch) == 1 and "A" <= ch <= "Z":
        return True
    return False


def is_digit(ch: str) -> bool:
    """Return True if ch is exactly one of the characters 0 to 9.

    Optional helper: you may delete it or write your own. Not unit-tested.
    """
    
    if len(ch) == 1 and "0" <= ch <= "9":
        return True
    return False


def normalise_plate(raw: str) -> str:
    """Return raw stripped, upper-cased, with every space and hyphen removed."""

    plate = raw.strip()
    plate = plate.replace(" ", "")
    plate = plate.replace("-", "")
    plate = plate.upper()
    return plate


def is_valid_plate(plate: str) -> bool:
    """Return True if the normalised plate satisfies every plate rule."""

    
    if len(plate) < 2:
        return False
    
    if plate[0] not in CATEGORY_LETTERS:
        return False
    
    pos = 1
    
    if plate[1] == BARBUDA_MARKER:
        pos += 1
    
    digits = plate[pos:]
    
    if len(digits) < MIN_DIGITS or len(digits) > MAX_DIGITS:
        return False
    
    for digit in digits:
        if not digit.isdigit():
            return False
    return True


def plate_category(plate: str) -> str:
    """Return the vehicle category named by the first letter of a valid plate."""
    
    if plate[0] == "P":
        return "Private"
    elif plate[0] == "T":
        return "Taxi"
    elif plate[0]  == "H":
        return "Hired"
    elif plate[0] == "R":
        return "Rental"
    elif plate[0] == "B":
        return "Bus"
    elif plate[0] == "G":
        return "Government"
    


def plate_island(plate: str) -> str:
    """Return "Barbuda" if a valid plate carries the X marker, else "Antigua"."""
    
    
    if "X" in plate:
        return "Barbuda"
    else:
        return "Antigua"


def matches_pattern(plate: str, pattern: str) -> bool:
    """Return True if the normalised plate matches the normalised pattern."""
    
    
    if len(plate) != len(pattern):
        return False

    for i in range (len(plate)):
        if pattern[i] == ANY_CHAR:
            continue
        elif pattern[i] == ANY_DIGIT:
            if not plate[i].isdigit():
                return False
        elif pattern[i] == ANY_LETTER:
            if not plate[i].isalpha():
                return False

        else:
            if plate[i] != pattern[i]:
                return False    
    return True    


def main() -> None:
    """Read a plate and a pattern, then print the checkpoint report."""
    
    raw = input("Enter plate: ")
    plate = normalise_plate(raw)
    print(f"Normalized plate: {plate}")
       
    if is_valid_plate(plate):
        print("Status: Valid")
        print(f"Category: {plate_category(plate)}")
        print(f"Island: {plate_island(plate)}")

        pattern_raw = input("Enter watch-list pattern: ")
        pattern = normalise_plate(pattern_raw)

        if matches_pattern(plate, pattern):
            print("Watch-list: FLAGGED ")
        else:
            print("Watch-list: Clear")

    
    else: 
        print("Status: Invalid")


if __name__ == "__main__":
    main()
