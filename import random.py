import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    # Random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    # Game loop
    while not guessed:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
