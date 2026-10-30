# Name: Stephan Jones
# Student ID: 500004652
# Date: 19th October 2026
# Question: Q1 Checkpoint Plate Reader - Part 1
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Normalise a licence plate and check its basic shape."""

MAX_LETTERS = 2
MIN_DIGITS = 1
MAX_DIGITS = 4


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
    plate = plate.replace (" ", "")
    plate = plate.replace ("-", "")
    plate = plate.upper()
    return plate



def is_valid_plate(plate: str) -> bool:
    """Return True if the normalised plate satisfies every plate rule."""
    i = 0
    while i < len(plate) and is_letter(plate[i]):
        i += 1
        if i < 1 or i > MAX_LETTERS:
            return False
        digit_count = 0

    if i >= len(plate) or plate[i] == "0":
        return False
    while i < len(plate) and is_digit(plate[i]):
        digit_count += 1
        i += 1
    if digit_count < MIN_DIGITS or digit_count > MAX_DIGITS:
        return False

    if i != len(plate):
        return False
    
    return True


def main() -> None:
    """Read a plate and print its normalised form and status."""
    
    raw = input("Enter plate: ")
    plate = normalise_plate(raw)
    print(f"Normalised plate: {plate}")

    if is_valid_plate(plate):
        print("Status: VALID")
    else: 
        print("Status: INVALID")


if __name__ == "__main__":
    main()
