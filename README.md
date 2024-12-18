# Guess the Number Game

## Introduction
The **Guess the Number** game is a simple interactive Python program where the user tries to guess a randomly generated number. The program provides hints if the guess is too high or too low, and the game continues until the correct number is guessed.

## Features
- **Random Number Generation**: A random number between 1 and 10 is chosen at the start of the game.
- **User Input**: The player inputs their guesses interactively.
- **Feedback**: The program guides the player with hints (“Too low!” or “Too high!”).
- **Attempts Tracker**: Displays the total number of attempts taken once the correct guess is made.
- **Input Validation**: Ensures that only valid integers are entered.

## Prerequisites
- Python 3 installed on your machine.

## How to Run the Program
1. Download the `guessthenumber.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the following command:

   ```bash
   python guessthenumber.py
   ```

## Example Gameplay
```plaintext
Welcome to the 'Guess the Number' game!
I have chosen a number between 1 and 100. Can you guess it?

Enter your guess: 5
Too low! Try again.

Enter your guess: 8
Too high! Try again.

Enter your guess: 7
Congratulations! You guessed it in 3 attempts.
```

## How It Works
1. The program generates a random number between 1 and 10 using the `random.randint()` function.
2. It enters a loop where the user inputs their guess.
3. The program compares the guess to the random number and provides feedback.
4. The loop continues until the user guesses correctly.

## Customization
- **Range**: To change the range of numbers, modify the line:
  ```python
  number_to_guess = random.randint(1, 10)
  ```
  For example, to use a range of 1 to 100, update it to:
  ```python
  number_to_guess = random.randint(1, 100)
  ```

## Possible Enhancements
- Add difficulty levels (e.g., Easy: 1–10, Medium: 1–50, Hard: 1–100).
- Limit the number of guesses.
- Display a score based on the number of attempts.

## License
This project is free to use and modify for personal or educational purposes.

