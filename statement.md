# Rock Paper Scissors – Project Statement

## 1. Problem Statement

The objective of this project is to develop a simple and interactive **Rock Paper Scissors game using Python**.

The game allows a user to play against the computer. The computer randomly selects Rock, Paper, or Scissors, while the user enters their choice. The program compares both choices and determines whether the user wins, loses, or the game ends in a tie.

The system should also handle invalid inputs, allow multiple rounds, and provide an option for the user to exit the game.

---

## 2. Scope of the Project

The scope of this project includes developing a basic command-line Rock Paper Scissors game.

The project covers:

* Displaying a welcome message.
* Accepting the user's choice.
* Generating a random choice for the computer.
* Comparing the user's choice with the computer's choice.
* Determining the winner.
* Displaying the result of each round.
* Handling invalid inputs.
* Allowing the user to play multiple rounds.
* Providing a `quit` option to exit the game.

The current version does not include a database, user accounts, or permanent score storage.

---

## 3. Target Users

The main target users of this project are:

* **Students** learning Python programming.
* **Beginners** who want to understand basic programming concepts.
* **Teachers/Faculty** demonstrating Python concepts through a simple project.
* **Casual users** who want to play a simple command-line game.

The project is especially suitable for beginners because it demonstrates fundamental Python concepts in a practical and interactive way.

---

## 4. High-Level Features

### 1. Welcome Message

The program displays a welcome message when the game starts.

### 2. User Input

The user can enter:

* `rock`
* `paper`
* `scissors`

### 3. Random Computer Choice

The computer randomly selects one of the three available choices using Python's `random` module.

### 4. Winner Determination

The program compares the two choices according to the standard rules:

* Rock beats Scissors.
* Scissors beats Paper.
* Paper beats Rock.
* Same choices result in a tie.

### 5. Input Validation

The program checks whether the user's input is valid. If an invalid choice is entered, the program displays an error message and asks the user to try again.

### 6. Multiple Rounds

The user can continue playing multiple rounds without restarting the program.

### 7. Exit Option

The user can enter `quit` to end the game.

### 8. Result Display

After every valid round, the program displays:

* User's choice
* Computer's choice
* Game result

---

## 5. Project Limitations

The current version of the project:

* Does not store scores permanently.
* Does not use a database.
* Does not have a graphical user interface.
* Supports only one user playing against the computer.
* Does not provide online multiplayer functionality.

These limitations can be addressed in future versions of the project.

---

## 6. Future Scope

The project can be enhanced by adding:

* Score tracking.
* Best-of-three or best-of-five game modes.
* Player names.
* Graphical user interface using Tkinter.
* Game statistics.
* Persistent score storage.
* Sound effects.
* Online multiplayer functionality.
