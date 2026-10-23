# Name: Stephan Jones
# Student ID: 500004652
# Date: 19th October 2026
# Question: Q2 Taxi Fuel Calculator - Part 2
# Collaborators: none
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Validate trip figures and compute the fuel cost of a taxi trip."""

LITRES_PER_GALLON = 3.785
CENTS_PER_DOLLAR = 100
ERROR_MESSAGE = "Invalid: enter a number greater than 0."


def litres_used(distance_km: float, km_per_litre: float) -> float:
    """Return the litres of fuel used to drive distance_km."""
    
    return distance_km / km_per_litre


def fuel_cost(litres: float, price_per_gallon: float) -> float:
    """Return the unrounded EC$ cost of the litres, priced per US gallon."""
    
    return litres / LITRES_PER_GALLON * price_per_gallon


def to_cents(amount: float) -> int:
    """Return amount (EC$) as a whole number of cents using round()."""
    
    return round(amount * CENTS_PER_DOLLAR)


def format_cents(cents: int) -> str:
    """Return a non-negative number of cents as a string with exactly 2 decimals."""
   
    return f"{cents / CENTS_PER_DOLLAR:.2F}"


def is_positive_number_text(text: str) -> bool:
    """Return True if text (after strip) is a plain decimal number greater than 0."""
    
    return text.strip().replace(".", "", 1).isdigit() and float(text) > 0


def read_positive_number(prompt: str) -> float:
    """Prompt until the user types a valid positive number, then return it."""
    
    while True:
        text = input(prompt)
        if is_positive_number_text(text):
            return float(text)
        print(ERROR_MESSAGE)


def main() -> None:
    """Read and validate the trip figures, then print the fuel report."""

    
    trip = read_positive_number("Trip distance (km): ")
    fuel = read_positive_number("Fuel efficiency (km per litre): ")
    price = read_positive_number("Price per gallon (EC$): ")
    
    litres = litres_used(trip, fuel)
    cost = fuel_cost(litres, price)
    cents = to_cents(cost)
    formatted_cost = format_cents(cents)
    
    print(f"Fuel used: {litres:.2f} litres")
    print(f"Fuel cost: EC${formatted_cost}")


if __name__ == "__main__":
    main()
