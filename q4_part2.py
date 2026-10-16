# Name: <your full name>
# Student ID: <your ID>
# Date: <date you started>
# Question: Q4 CHOGM Credential Checker - Part 2
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Validate the format and checksum of a CHOGM delegate credential code."""

CODE_LENGTH = 10
FIRST_LETTER_WEIGHT = 7
SECOND_LETTER_WEIGHT = 6
FIRST_DIGIT_WEIGHT = 5
CHECK_MODULUS = 11
TEN_SYMBOL = "X"


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


def normalise_credential(raw: str) -> str:
    """Return raw with leading/trailing whitespace removed, in upper case."""
    # TODO: replace 'pass' with your code.
    pass


def is_valid_format(code: str) -> bool:
    """Return True if a normalised code has the shape LL-DDDDD-C."""
    # TODO: replace 'pass' with your code.
    pass


def letter_value(ch: str) -> int:
    """Return the position of an uppercase letter in the alphabet (A=1 ... Z=26)."""
    # TODO: replace 'pass' with your code.
    pass


def expected_check_char(code: str) -> str:
    """Return the check character that a correctly formatted code should end with."""
    # TODO: replace 'pass' with your code.
    pass


def checksum_ok(code: str) -> bool:
    """Return True if a correctly formatted code ends with its expected check character."""
    # TODO: replace 'pass' with your code.
    pass


def main() -> None:
    """Read a credential code and print its format and checksum result."""
    # TODO: replace 'pass' with your code.
    pass


if __name__ == "__main__":
    main()
