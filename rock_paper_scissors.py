import random

user_score = 0
computer_score = 0
draws = 0
options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Type Rock, Paper, Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Type a valid option.")
        continue
    
    random_number = random.randint(0,2) # 0:rock, 1:paper, 2:scissors
    computer_option = options[random_number]
    print("Computer picked:", computer_option)

    if user_input == computer_option:
        print("Draw!")
        draws += 1
    elif user_input == options[0] and computer_option == options[2]:
        print("You won!")
        user_score += 1
    elif user_input == options[1] and computer_option == options[0]:
        print("You won!")
        user_score += 1
    elif user_input == options[2] and computer_option == options[1]:
        print("You won!")
        user_score += 1
    else:
        print("You lost")
        computer_score += 1

if user_score > computer_score:
    print("You won! The score is - You:",user_score, "to Computer:", computer_score, "Draws:", draws)
else:
    print("You lost... The score is - You:",user_score, "to Computer:", computer_score, "Draws:", draws)

print("Goodbye!")
