# Vityarthi-Project
Rock Paper Scissors game
My project includes control-if statements and displaying interactive results for a user friendly environment.
# Rock Paper Scissors

## 1. Project Title

**Rock Paper Scissors Game**

A simple command-line Rock Paper Scissors game developed using Python, where the user plays against the computer.

---

## 2. Project Overview

Rock Paper Scissors is a popular two-player game based on three choices: **Rock, Paper, and Scissors**.

In this project, the user plays against the computer. The computer randomly selects one of the three choices, and the program compares it with the user's choice to determine the result.

The program displays a welcome message when it starts and allows the user to play multiple rounds. The user can enter **`quit`** at any time to exit the game.

### Game Rules

* **Rock beats Scissors**
* **Scissors beats Paper**
* **Paper beats Rock**
* If both players choose the same option, the result is a **Tie**

---

## 3. Features

The project includes the following features:

* Welcome message for the user
* User can choose Rock, Paper, or Scissors
* Computer makes a random choice
* Automatic winner determination
* Displays the user's choice
* Displays the computer's choice
* Displays the game result
* Handles invalid user input
* Allows multiple rounds
* Provides a `quit` option to exit the game
* Simple and beginner-friendly command-line interface

---

## 4. Technologies / Tools Used

### Programming Language

* **Python 3**

### Python Concepts Used

* Variables
* Lists
* `input()` function
* `print()` function
* `if`, `elif`, and `else` statements
* `while` loop
* `break` statement
* String `.lower()` method
* Random selection

### Python Module Used

```python
random
```

The `random` module is used to randomly select the computer's choice.

### Development Tools

The project can be developed and executed using:

* Visual Studio Code
* IDLE
* PyCharm
* Python Command Prompt
* Any other Python-supported IDE

---

## 5. Project Structure

```text
Rock-Paper-Scissors/
│
├── main.py
└── README.md
```

### `main.py`

Contains the complete Python source code for the Rock Paper Scissors game.

### `README.md`

Contains information about the project, features, installation, execution, and testing instructions.

---

## 6. Steps to Install & Run the Project

### Step 1: Install Python

Install **Python 3** on your computer if it is not already installed.

To check whether Python is installed, open a terminal or command prompt and run:

```bash
python --version
```

or:

```bash
python3 --version
```

---

### Step 2: Download or Clone the Project

Download the project files and place them in a folder named:

```text
Rock-Paper-Scissors
```

The folder should contain:

```text
main.py
README.md
```

---

### Step 3: Open the Project

Open the project folder using your preferred Python editor, such as Visual Studio Code.

---

### Step 4: Run the Program

Open the terminal inside the project folder and run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

---

## 7. How to Play

After starting the program, the user will see a welcome message:

```text
================================
  Welcome to Rock Paper Scissors!
================================
Let's start the game!
```

The program will then ask:

```text
Enter rock, paper, or scissors (or 'quit' to exit):
```

Enter one of the following:

```text
rock
paper
scissors
```

The computer will randomly select its choice.

For example:

```text
You chose: rock
Computer chose: scissors
You win!
```

To exit the game, enter:

```text
quit
```

The program will display:

```text
Thanks for playing! Goodbye!
```

---

## 8. Instructions for Testing

The program should be tested with different inputs to make sure all possible situations work correctly.

### Test Case 1: User Wins

**Input:**

```text
rock
```

**Computer Choice:**

```text
scissors
```

**Expected Output:**

```text
You win!
```

---

### Test Case 2: Computer Wins

**Input:**

```text
rock
```

**Computer Choice:**

```text
paper
```

**Expected Output:**

```text
Computer wins!
```

---

### Test Case 3: Tie

**Input:**

```text
paper
```

**Computer Choice:**

```text
paper
```

**Expected Output:**

```text
It's a tie!
```

---

### Test Case 4: Invalid Input

**Input:**

```text
apple
```

**Expected Output:**

```text
Invalid choice! Please try again.
```

The program should continue running and ask the user for another choice.

---

### Test Case 5: Exit Program

**Input:**

```text
quit
```

**Expected Output:**

```text
Thanks for playing! Goodbye!
```

---

## 9. Sample Output

```text
================================
  Welcome to Rock Paper Scissors!
================================
Let's start the game!

Enter rock, paper, or scissors (or 'quit' to exit): rock

You chose: rock
Computer chose: scissors
🎉 You win!

--------------------------------

Enter rock, paper, or scissors (or 'quit' to exit): paper

You chose: paper
Computer chose: scissors
Computer wins!

--------------------------------

Enter rock, paper, or scissors (or 'quit' to exit): quit

Thanks for playing! Goodbye!
```

---



## 10. Future Enhancements

The project can be improved in the future by adding:

* Score tracking
* Number of rounds
* Best-of-three or best-of-five mode
* Player name
* Graphical User Interface (GUI)
* Game statistics
* Sound effects
* Saving scores to a file
* Rock-Paper-Scissors-Lizard-Spock mode

---

## 11. Conclusion

The Rock Paper Scissors project demonstrates the use of basic Python programming concepts to create an interactive command-line game.

The project uses user input, conditional statements, loops, lists, and the `random` module. It also demonstrates input validation and repeated gameplay.

This project provides a simple practical application of Python programming fundamentals.
