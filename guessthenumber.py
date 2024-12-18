import random

def guess_number():
    print("Welcome to the 'Guess the Number' game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_number()
