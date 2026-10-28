# Name: Stephan Jones
# Student ID: 500004652
# Date: 25th October 2026
# Question: Q4 CHOGM Credential Validator - Part 1
# Collaborators: none 
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Validate the format of a CHOGM delegate credential code."""

CODE_LENGTH = 10
TEN_SYMBOL = "X"


def is_letter(ch: str) -> bool:
    """Return True if ch is exactly one uppercase letter from A to Z.

    Optional helper: you may delete it or write your own. Not unit-tested.
    """
    
    if ch >= "A" and ch <= "Z":
        return True
    return False


def is_digit(ch: str) -> bool:
    """Return True if ch is exactly one of the characters 0 to 9.

    Optional helper: you may delete it or write your own. Not unit-tested.
    """
    
    if ch >= "0" and ch <= "9":
        return True
    return False


def normalise_credential(raw: str) -> str:
    """Return raw with leading/trailing whitespace removed, in upper case."""

    return raw.strip().upper()


def is_valid_format(code: str) -> bool:
    """Return True if a normalised code has the shape LL-DDDDD-C."""

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"

    if len(code) != CODE_LENGTH:                       # exactly 10 characters
        return False
    if code[0] not in letters or code[1] not in letters:   # characters 1-2
        return False
    if code[2] != "-":                        # character 3
        return False
    for i in range(3, 8):                     # characters 4-8 (index 3 to 7)
        if code[i] not in digits:
            return False
    if code[8] != "-":                        # character 9
        return False
    if code[9] not in digits and code[9] != TEN_SYMBOL:   # character 10
        return False
    return True


def main() -> None:
    """Read a credential code and print whether its format is OK."""

    credential_code = input("Enter credential code: ")
    credential_code = normalise_credential(credential_code)
    print(f"Credential: {credential_code}")

    if is_valid_format(credential_code):
        print("OK")
    else:
        print("Bad")


if __name__ == "__main__":
    main()
