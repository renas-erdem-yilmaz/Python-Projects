# Password Strength Checker

A simple Python program that evaluates password strength based on five criteria and provides suggestions for improvement.

## Features

- Checks password length, uppercase and lowercase letters, digits, and special characters.
- Calculates a strength score from 0 to 5.
- Classifies passwords from Very Weak to Very Strong.
- Detects some commonly used passwords.
- Allows users to check multiple passwords in one session.
- Handles empty inputs.

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

Enter a password to check its strength, or type `exit` to quit.

## Example Output

```text
Enter your password: Hello123

Try to make it at least 12 characters long!
Try to use special characters!

Password Strength: Moderate
Score: 3/5
```

## Technologies

- Python 3
- No external libraries required

## What I Learned

- String methods and generator expressions
- Input validation
- Functions and conditional statements
- Loops and basic program flow

*Note: This is an educational project and does not provide a comprehensive security assessment of passwords.*
