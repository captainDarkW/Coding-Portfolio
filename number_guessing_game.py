import random

while True:
    print("Hello! I'm your computer. What is your name? ")
    user_name = input().title()
    print("Well, " + user_name + ", I would like to play a number guessing game. ")
    tries = 6
    computer_number = random.randint(1, 20)
    print("I am thinking of a number between 1 and 20.")
    while tries > 0:
        while True:
            try:
                print("What is your guess of my number? You have", (tries), "guesses left.")
                guess_value = int(input())
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        if guess_value < computer_number:
            print("Your guess is too low. ")
            tries -= 1
        if guess_value > computer_number:
            print('Your guess is too high.')
            tries -= 1
        if guess_value == computer_number:
            break
    if guess_value == computer_number:
        print("Congratulations, "+ user_name + "! You guessed my number with only " + str(tries-1) + " guesses remaining!")
    if guess_value != computer_number:
        computer_number = str(computer_number)
        print("YAY! I win! The number I was thinking of was " + computer_number)
    print("Thank you for playing with me,", user_name + ".")
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break
