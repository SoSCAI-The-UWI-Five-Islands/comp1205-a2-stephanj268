# Name: Stephan Jones
# Student ID: 500004652
# Date: 19th October 2026
# Question: Q2 Taxi Fuel Calculator - Part 1
# Collaborators: none
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>
"""Compute the fuel cost of a taxi trip."""

LITRES_PER_GALLON = 3.785
CENTS_PER_DOLLAR = 100


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


def main() -> None:
    """Read the trip figures, then print the fuel report."""
    
    trip = float(input("Trip distance (km): "))
    fuel = float(input("Fuel efficiency (km per litre): "))
    price = float(input("Price per gallon (EC$): "))

    litres = litres_used(trip, fuel)
    cost = fuel_cost(litres, price)
    cents = to_cents(cost)
    formatted_cost = format_cents(cents)

    print(f"Fuel used: {litres:.2f} litres")
    print(f"Fuel cost: EC${formatted_cost}")



if __name__ == "__main__":
    main()
