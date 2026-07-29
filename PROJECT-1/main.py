import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
yourDict = {'rock': 0, 'paper': 1, 'scissors': 2}
computer_value = yourDict[computer_choice]
reverseDict = {0: 'rock', 1: 'paper', 2: 'scissors'}
your_value = yourDict[input("Enter your choice (rock, paper, scissors): ")]

if your_value == computer_value:
    print(f"Both chose {reverseDict[your_value]}. It's a tie!")
elif (your_value - computer_value) % 3 == 1:
    print(f"You chose {reverseDict[your_value]} and the computer chose {reverseDict[computer_value]}. You win!")
else:
    print(f"You chose {reverseDict[your_value]} and the computer chose {reverseDict[computer_value]}. You lose!")
    