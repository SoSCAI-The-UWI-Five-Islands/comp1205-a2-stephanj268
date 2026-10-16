# Name: <your full name>
# Student ID: <your ID>
# Date: <date you started>
# Question: Q1 Checkpoint Plate Reader - Part 2
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Normalise and validate a licence plate, then report its category and island."""

CATEGORY_LETTERS = "PTHRBG"
BARBUDA_MARKER = "X"
MAX_LETTERS = 2
MIN_DIGITS = 1
MAX_DIGITS = 4


def is_letter(ch: str) -> bool:
    """Return True if ch is exactly one uppercase letter from A to Z.

    Optional helper: you may delete it or write your own. Not unit-tested.
    """
    # TODO: replace 'pass' with your code.
    pass


def is_digit(ch: str) -> bool:
    """Return True if ch is exactly one of the characters 0 to 9.

    Optional helper: you may delete it or write your own. Not unit-tested.
    """
    # TODO: replace 'pass' with your code.
    pass


def normalise_plate(raw: str) -> str:
    """Return raw stripped, upper-cased, with every space and hyphen removed."""
    # TODO: replace 'pass' with your code.
    pass


def is_valid_plate(plate: str) -> bool:
    """Return True if the normalised plate satisfies every plate rule."""
    # TODO: replace 'pass' with your code.
    pass


def plate_category(plate: str) -> str:
    """Return the vehicle category named by the first letter of a valid plate."""
    # TODO: replace 'pass' with your code.
    pass


def plate_island(plate: str) -> str:
    """Return "Barbuda" if a valid plate carries the X marker, else "Antigua"."""
    # TODO: replace 'pass' with your code.
    pass


def main() -> None:
    """Read a plate and print its status, category and island."""
    # TODO: replace 'pass' with your code.
    pass


if __name__ == "__main__":
    main()
