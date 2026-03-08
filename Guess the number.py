#Guess the number

import random

x = int(input("What should the number be from? "))
guesses = int(input("How many guesses do you want?: "))

number = random.randint(1, x)
guesses_left = guesses
hint_given = False
hint_threshold = 3  # Set the number of incorrect guesses required before giving a hint

while guesses_left > 0:
    guess = int(input(f"Guess the number between 1 and {x}: "))

    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    guesses_left -= 1
    hint_threshold -=1

    # Provide hints
    if guesses_left == guesses - 1:
        if number % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
    elif guesses_left == guesses - 2:
        if number < 2:
            print("Hint: The number is not prime.")
        else:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("Hint: The number is prime.")
            else:
                print("Hint: The number is composite.")


    if guesses_left  and guesses >= 10 and not hint_given and hint_threshold == 0 and x <= 25:

        hint_low = max(1, number - 10)
        hint_high = min(x, number + 10)
        print(f"Hint: The number is between {hint_low} and {hint_high}.")
        hint_given = True
if guesses_left == 0:
    print("Sorry, you ran out of guesses. The number was", number)