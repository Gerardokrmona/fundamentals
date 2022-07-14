import random

#-- EJERCICIO DE CODIFICACIÓN LOTERIA

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

print(lottery_numbers)

winner ={"name" : "no_name", "got" : 0}

for index in range(4):
    
    numbers_right = len(players[index]["numbers"].intersection(lottery_numbers))
    
    if numbers_right > winner["got"]:
        winner["name"] = players[index]["name"]
        winner["got"] = numbers_right
        
winner_name = winner["name"]
winnings = 100**winner["got"]
print(f"{winner_name} won {winnings}")