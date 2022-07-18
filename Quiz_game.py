print("Welcome to my quiz game!!")

playing = input("Are you ready to play? (y/n) ")

if playing.lower() != "y":
    print("Bye!")
    quit()

print("Let's start! :) ")

counter = 0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    counter += 1
else:
    print("Wrong!")
    counter -= 1

answer = input("What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    counter += 1
else:
    print("Wrong!")
    counter -= 1

answer = input("What is the capital of Rajasthan? ")
if answer.lower() == "jaipur":
    print("Correct!")
    counter += 1
else:
    print("Wrong!")
    counter -= 1

answer = input("What is the capital of USA? ")
if answer.lower() == "washington":
    print("Correct!")
    counter += 1
else:
    print("Wrong!")
    counter -= 1

print("Your score is", counter)
print("you got",(counter)/4*100,"%")
print("Thanks for playing!")
