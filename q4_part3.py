# Name: Paul Giddings
# Student ID: 500004577
# Date: 24/11/2026
# Question: Q4 CHOGM Credential Checker - Part 3
# Collaborators: None
# Tools used: Copilot
"""Validate a CHOGM delegate credential code and decide access to a venue zone."""

CODE_LENGTH = 10
FIRST_LETTER_WEIGHT = 7
SECOND_LETTER_WEIGHT = 6
FIRST_DIGIT_WEIGHT = 5
CHECK_MODULUS = 11
TEN_SYMBOL = "X"
HOST_DELEGATION = "AG"


def is_letter(ch: str) -> bool:

   if ch >= "A" and ch <= "Z":
       return True 
   return False 


def is_digit(ch: str) -> bool:
   
   if ch >= "0" and ch <= "9":
       return True
   return False
   

def normalise_credential(raw: str) -> str:
    """Return raw with leading/trailing whitespace removed, in upper case."""
    return raw.strip().upper()


def is_valid_format(code: str) -> bool:
    """Return True if a normalised code has the shape LL-DDDDD-C."""
    if len(code) != CODE_LENGTH:
      return False

  if not is_letter(code[0]) or not is_letter(code[1]):
      return False 
  if code[2] != "-":
      return False

  for i in range(3,8):
      if not is_digit(code[i]):
          return False

   if code[8] != "-":
        return False

  if not is_digit(code[9]) and code[9] != TEN_SYMBOL: 
      return False

  return True 
      


def letter_value(ch: str) -> int:
    """Return the position of an uppercase letter in the alphabet (A=1 ... Z=26)."""

    return ord(ch) - ord("A") + 1


def expected_check_char(code: str) -> str:
    """Return the check character that a correctly formatted code should end with."""

    total = 0 

    total += letter_value(code[0]) * FIRST_LETTER_WEIGHT
    total += letter_value(code[1]) * SECOND_LETTER_WEIGHT

    total += int(code[3]) * FIRST_DIGIT_WEIGHT
    total += int(code[4]) * 4
    total += int(code[5]) * 3
    total += int(code[6]) * 2
    total += int(code[7]) * 1

    remainder = total % CHECK_MODULUS 

    if remainder == 10: 
        return TEN_SYMBOL
    else:
        return str(remainder) 


def checksum_ok(code: str) -> bool:
    """Return True if a correctly formatted code ends with its expected check character."""
    return code[9] == expected_check_char(code) 
    
def credential_role(code: str) -> str:
    """Return the role named by the first digit of a valid code."""

    if code[3] == "1":
        return "Head of Government"
    elif code[3] == "2":
        return "Minister"
    elif code[3] == "3":
        return "Official"
    elif code[3] == "4":
        return "Media"
    else:
        return "Support Staff"


def is_known_zone(zone: str) -> bool:
    """Return True if zone is PLENARY, RETREAT, MEDIA or VENUE."""

    if zone == "PLENARY":
        return True
    elif zone == "RETREAT":
        return True
    elif zone == "MEDIA":
        return True
    elif zone == "VENUE":
        return True
    else:
        return False


def zone_allowed(code: str, zone: str) -> bool:
    """Return True if the holder of a valid code may enter the normalised zone."""

    if not is_known_zone(zone):
        return False

    if code[3] == "1":
        return True

    elif code[3] == "2":
        if zone == "PLENARY" or zone == "MEDIA" or zone == "VENUE":
            return True
        elif zone == "RETREAT" and code[0:2] == HOST_DELEGATION:
            return True

    elif code[3] == "3":
        if zone == "PLENARY" or zone == "VENUE":
            return True

    elif code[3] == "4":
        if zone == "MEDIA" or zone == "VENUE":
            return True

    else:
        if zone == "VENUE":
            return True

    return False


def main() -> None:
    """Read a credential code (and a zone if it is genuine) and print the decision."""

    credential_code = input("Enter credential code: ")
    credential_code = normalise_credential(credential_code)

    print(f"Credential: {credential_code}")

    if not is_valid_format(credential_code):
        print("Format: BAD")
        return

    print("Format: OK")

    if not checksum_ok(credential_code):
        expected = expected_check_char(credential_code)
        print(f"Checksum: FAIL (expected {expected})")
        return

    print("Checksum: PASS")

    role = credential_role(credential_code)
    print(f"Role: {role}")

    zone = input("Zone requested: ")
    zone = zone.strip().upper()

    if not is_known_zone(zone):
        print("Access: DENIED (unknown zone)")
    elif zone_allowed(credential_code, zone):
        print("Access: GRANTED")
    else:
        print("Access: DENIED")


if __name__ == "__main__":
    main()

