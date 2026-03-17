"""This code is a simulation of the Birthday Paradox—the
counterintuitive mathematical fact that in a group of just 23 people,
there is a 50% chance that at least two of them share a birthday."""

import datetime
import random
from typing import List, Optional

class BirthdaySimulator:
    """A class to simulate and calculate the Birthday Paradox probabilities."""

    def __init__(self, group_size: int, is_leap_year: bool = False):
        self.group_size = group_size
        self.days_in_year = 366 if is_leap_year else 365
        self.start_date = datetime.date(2020, 1, 1)

    def generate_birthdays(self) -> List[datetime.date]:
        """Generates a list of random date objects."""
        return [
            self.start_date + datetime.timedelta(random.randint(0, self.days_in_year - 1))
            for _ in range(self.group_size)
        ]

    @staticmethod
    def find_match(birthdays: List[datetime.date]) -> Optional[datetime.date]:
        """Returns the first duplicate date found, or None if all are unique."""
        seen = set()
        for date in birthdays:
            if date in seen:
                return date
            seen.add(date)
        return None

    def run_monte_carlo(self, iterations: int = 100_000) -> float:
        """Runs the simulation multiple times and returns the probability percentage."""
        match_count = 0
        for i in range(iterations):
            # Feature: Simple progress indicator
            if i % (iterations // 10) == 0:
                print(f"Progress: { (i / iterations) * 100:.0f}%...")
            
            if self.find_match(self.generate_birthdays()):
                match_count += 1
        
        return round((match_count / iterations) * 100, 2)

# --- Execution Block ---
if __name__ == "__main__":
    print("--- Birthday Paradox High-Speed Simulator ---")
    
    # Input validation
    try:
        size = int(input("Enter group size (1-100): "))
        sim = BirthdaySimulator(group_size=size)
        
        print(f"\nRunning {100_000:,} simulations for a group of {size}...")
        prob = sim.run_monte_carlo()
        
        print(f"\nResult: There is a {prob}% chance of a shared birthday.")
    except ValueError:
        print("Please enter a valid number.")