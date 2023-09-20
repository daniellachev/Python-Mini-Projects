print("Welcome to my quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

score = 0

answer = input("What is 2+2? ")
if answer.lower() == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is 1+1? ")
if answer.lower() == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Do you like girls? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("Is it day? ")
if answer.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "/4 or " + str(score / 4 * 100) + "%")
