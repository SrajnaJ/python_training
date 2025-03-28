import random

#Number Guessing Game:
secret_number=random.randint(1,100)
attempts=0

print("I've chosen a number between 1-100")
print("Try to guess the number!!")

attempts=0

while True:
    try:
        guess=int(input("Enter your guess: "))
        attempts=attempts+1

        if guess==secret_number:
            print(f"Congratulations! you guessed the number {secret_number} in {attempts} attempts!")
            break

        elif guess<secret_number:
            print("Your guess is too low! Try Again.")
        
        else:
            print("Your guess is too high! Try Again.")
    except ValueError:
        print("Enter a valid guess!")