# Name: <your full name>
# Student ID: <your ID>
# Date: <date you started>
# Question: Q5 (Bonus) Motorcade Log - Part 2
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Rebuild a motorcade's distance from a speed log, rejecting impossible entries."""

MINUTES_PER_HOUR = 60
MAX_SPEED = 120
SPEED_LIMIT = 80


def is_all_digits(text: str) -> bool:
    """Return True if text is non-empty and every character is one of 0 to 9.

    Optional helper: you may delete it or write your own. Not unit-tested.
    """
    # TODO: replace 'pass' with your code.
    pass


def is_valid_entry_text(line: str) -> bool:
    """Return True if line holds two non-negative integers separated by spaces."""
    # TODO: replace 'pass' with your code.
    pass


def parse_speed(line: str) -> int:
    """Return the speed (km/h), the first number on a valid entry line."""
    # TODO: replace 'pass' with your code.
    pass


def parse_minutes(line: str) -> int:
    """Return the minutes since departure, the second number on a valid entry line."""
    # TODO: replace 'pass' with your code.
    pass


def segment_distance(speed_kmh: int, elapsed_minutes: int) -> float:
    """Return the km covered at speed_kmh for elapsed_minutes."""
    # TODO: replace 'pass' with your code.
    pass


def main() -> None:
    """Read the motorcade log and print the distance and speeding count."""
    # TODO: replace 'pass' with your code.
    pass


if __name__ == "__main__":
    main()
