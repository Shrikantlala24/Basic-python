import random

def number_guess():
    num_to_guess = random.randint(1, 100)
    attempt = 0
    guessed = False

    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        try:
            num = int(input("Take a guess: "))
            attempt += 1

            if num < num_to_guess:
                print("Too low, try again.")
            elif num > num_to_guess:
                print("Too high, try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {num_to_guess} in {attempt} attempts.")
                guessed = True
        except ValueError:
            print("❗ Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guess()
