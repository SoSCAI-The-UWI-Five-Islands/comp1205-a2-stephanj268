# Name: <your full name>
# Student ID: <your ID>
# Date: <date you started>
# Question: Q2 Taxi Fuel Calculator - Part 3
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Validate trip figures, compute the fuel cost of a taxi trip and compare it with the fare."""

LITRES_PER_GALLON = 3.785
CENTS_PER_DOLLAR = 100
ERROR_MESSAGE = "Invalid: enter a number greater than 0."


def litres_used(distance_km: float, km_per_litre: float) -> float:
    """Return the litres of fuel used to drive distance_km."""
    # TODO: replace 'pass' with your code.
    pass


def fuel_cost(litres: float, price_per_gallon: float) -> float:
    """Return the unrounded EC$ cost of the litres, priced per US gallon."""
    # TODO: replace 'pass' with your code.
    pass


def to_cents(amount: float) -> int:
    """Return amount (EC$) as a whole number of cents using round()."""
    # TODO: replace 'pass' with your code.
    pass


def format_cents(cents: int) -> str:
    """Return a non-negative number of cents as a string with exactly 2 decimals."""
    # TODO: replace 'pass' with your code.
    pass


def is_positive_number_text(text: str) -> bool:
    """Return True if text (after strip) is a plain decimal number greater than 0."""
    # TODO: replace 'pass' with your code.
    pass


def read_positive_number(prompt: str) -> float:
    """Prompt until the user types a valid positive number, then return it."""
    # TODO: replace 'pass' with your code.
    pass


def trip_result(fare_cents: int, cost_cents: int) -> str:
    """Return the PROFIT / LOSS / BREAK-EVEN description for a trip."""
    # TODO: replace 'pass' with your code.
    pass


def main() -> None:
    """Read and validate the trip figures, then print the fuel report."""
    # TODO: replace 'pass' with your code.
    pass


if __name__ == "__main__":
    main()
