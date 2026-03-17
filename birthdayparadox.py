"""This code is a simulation of the Birthday Paradox—the
counterintuitive mathematical fact that in a group of just 23 people,
there is a 50% chance that at least two of them share a birthday."""

import datetime
import random


def get_birthdays(number_of_birthdays):
    """Return a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all birthdays are in the same year.
        start_of_year = datetime.date(2020, 1, 1)

        # Get a random day of the year.
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Return the date object of a birthday that occurs more then once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.
    
    # Compare each birthday to every other birthday.
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a  # Return the matching birthday.
            

# Display the intro message.
print('''Birthday Paradox''')

# Set up a tuple of month names in order.
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        number_of_birthdays = int(response)
        break  # User has entered a valid amount.
print()

# Generate and display the birthdays.
print('Here are', number_of_birthdays, 'birthdays:')
birthdays = get_birthdays(number_of_birthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')

print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results.
print('In this simulation, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print('multiple people have a birthday on', date_text)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations.
print('Generating', number_of_birthdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
sim_match = 0  # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations.
    if i % 10_000 == 0:
        print(f'{i} simulations run...')
    birthdays = get_birthdays(number_of_birthdays)
    if get_match(birthdays) != None:
        sim_match += 1
print('100,000 simulations run.')

# Display simulation results.
probability = round(sim_match / 100_000 * 100, 2)
print(f'Out of 100,000 simulations of {number_of_birthdays} people, there was a')
print(f'matching birthday in that group {sim_match} times. This means')
print(f'that {number_of_birthdays} people have a {probability}% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')