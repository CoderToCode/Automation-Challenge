import random

# Generating the random number
number = random.randint(1, 10)


number_of_guesses = 0
print("Can you guess the number between 1 and 10?")

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Your guess is low")
    if guess > number:
        print("Your guess is high")
    if guess == number:
        print("You guessed the number in", number_of_guesses, "attempts!")
        break
else:
    print("You did not guess the number! The number is", number)