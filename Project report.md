# PROJECT REPORT

# NUMBER GUESSING GAME USING PYTHON

---

# Submitted By

**Name:** Saumya Thakur

**Course:** Python Programming

**Project Title:** Number Guessing Game

**Language Used:** Python

**Development Environment:** PyCharm / VS Code

**Version:** 1.0

---

# CERTIFICATE

This is to certify that **Saumya Thakur** has successfully completed the project entitled **"Number Guessing Game Using Python"**. The project has been developed using Python programming language and demonstrates the practical implementation of random number generation, loops, conditional statements, and exception handling.

The project fulfills all the requirements and objectives specified for the assignment.

---

# ACKNOWLEDGEMENT

I would like to express my sincere gratitude to my teachers, mentors, and all those who guided me throughout the development of this project.

Their valuable suggestions and encouragement helped me understand Python programming concepts and successfully complete this project.

I also thank the Python developer community for providing excellent documentation and learning resources.

---

# ABSTRACT

The Number Guessing Game is a simple console-based Python application designed to provide an interactive gaming experience while demonstrating fundamental programming concepts.

The program randomly generates a secret number between 1 and 100. The player attempts to guess the number within a limited number of attempts. After each guess, the program provides feedback indicating whether the entered number is too high or too low.

The project incorporates random number generation, loops, conditional statements, input validation, and exception handling, making it an ideal beginner-level Python application.

---

# INTRODUCTION

Games are one of the most effective ways to learn programming because they combine logic, user interaction, and problem-solving skills.

The Number Guessing Game is a classic example used by beginners to understand Python fundamentals. The program selects a random number and challenges the user to identify it through multiple attempts.

The game provides hints after each attempt, helping users improve their guessing strategy while making the experience engaging and educational.

---

# PROBLEM STATEMENT

Develop a Python application that:

* Generates a random number between 1 and 100.
* Allows the user to guess the number.
* Provides feedback for incorrect guesses.
* Limits the number of attempts.
* Displays a winning message if guessed correctly.
* Ends the game after maximum attempts are reached.

---

# OBJECTIVES

The main objectives of this project are:

1. To understand Python programming fundamentals.
2. To implement random number generation.
3. To develop logical thinking and problem-solving skills.
4. To practice loops and conditional statements.
5. To handle user inputs and exceptions.
6. To create an interactive console-based application.

---

# SOFTWARE REQUIREMENTS

## Hardware Requirements

* Processor: Intel i3 or higher
* RAM: 4 GB or above
* Storage: 100 MB free space

## Software Requirements

* Operating System: Windows/Linux/macOS
* Python 3.x
* PyCharm or Visual Studio Code
* Git and GitHub (Optional)

---

# TECHNOLOGIES USED

## Python

Python is a high-level programming language known for its simplicity and readability.

## Random Module

The random module is used to generate unpredictable numbers during program execution.

### Function Used

```python
random.randint(1,100)
```

This function generates a random integer between 1 and 100.

---

# SYSTEM DESIGN

## Input

* User's guessed number

## Process

* Generate random number
* Compare user guess with secret number
* Display hints
* Track attempts

## Output

* Too High
* Too Low
* Congratulations Message
* Game Over Message

---

# ALGORITHM

### Step 1

Import the random module.

### Step 2

Generate a random number between 1 and 100.

### Step 3

Set maximum attempts.

### Step 4

Ask the user to enter a guess.

### Step 5

Compare guess with secret number.

### Step 6

If guess is lower, display "Too Low".

### Step 7

If guess is higher, display "Too High".

### Step 8

If guess is correct, display winning message and terminate.

### Step 9

Repeat until maximum attempts are exhausted.

### Step 10

Display Game Over message if attempts are exhausted.

---

# FLOWCHART

Start

↓

Generate Random Number

↓

Enter Guess

↓

Is Guess Correct?

├── Yes → Display Congratulations → End

└── No

↓

Too High or Too Low

↓

Attempts Remaining?

├── Yes → Enter Guess Again

└── No → Display Game Over

↓

End

---

# SOURCE CODE

```python
import random

print("=" * 50)
print("NUMBER GUESSING GAME")
print("=" * 50)

secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!")

        elif guess > secret_number:
            print("Too High!")

        else:
            print("Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")

else:
    print("Game Over!")
    print(f"The correct number was {secret_number}")
```

---

# OUTPUT SCREENS

## Screen 1 – Program Start

[Insert Screenshot Here]

---

## Screen 2 – Winning Screen

[Insert Screenshot Here]

---

## Screen 3 – Game Over Screen

[Insert Screenshot Here]

---

# TESTING

| Test Case        | Input                  | Expected Result | Status |
| ---------------- | ---------------------- | --------------- | ------ |
| Valid Guess      | 50                     | Too High/Low    | Pass   |
| Correct Guess    | Secret Number          | Win Message     | Pass   |
| Invalid Input    | abc                    | Error Message   | Pass   |
| Maximum Attempts | Multiple Wrong Guesses | Game Over       | Pass   |

---

# ADVANTAGES

* Easy to understand.
* Beginner-friendly project.
* Demonstrates core Python concepts.
* Interactive user experience.
* Lightweight and fast execution.

---

# LIMITATIONS

* Console-based interface only.
* No score tracking.
* No difficulty levels.
* Single-player game.

---

# FUTURE ENHANCEMENTS

* Add graphical user interface using Tkinter.
* Implement score tracking system.
* Add difficulty levels.
* Save high scores in a file.
* Add multiplayer functionality.
* Add timer-based challenges.
* Develop a web-based version using Flask.

---

# LEARNING OUTCOMES

Through this project, I learned:

* Python syntax and structure.
* Random number generation.
* Conditional statements.
* Looping concepts.
* Exception handling.
* User input validation.
* Software documentation practices.
* GitHub project management.

---

# CONCLUSION

The Number Guessing Game successfully demonstrates the implementation of fundamental Python programming concepts through an interactive application.

The project achieves its objectives by generating random numbers, accepting user input, providing intelligent feedback, and handling exceptions effectively. It serves as an excellent beginner-level project for understanding logical programming and software development practices.

The project can be further enhanced with graphical interfaces, scoring systems, and advanced gameplay features, making it a strong foundation for future Python development projects.

---

# REFERENCES

1. Python Official Documentation – https://docs.python.org
2. Python Random Module Documentation
3. GitHub Documentation
4. PyCharm Documentation
5. Visual Studio Code Documentation

---

# THANK YOU
