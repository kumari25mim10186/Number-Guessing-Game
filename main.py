import random

print("=" * 50)
print("      NUMBER GUESSING GAME")
print("=" * 50)

secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0

print("\nI have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!\n")

        elif guess > secret_number:
            print("Too High!\n")

        else:
            print("\nCongratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")

else:
    print("\nGame Over!")
    print(f"The correct number was {secret_number}")
