import random

# Generate a random number between 1 and 100 and store it in a variable
n = random.randint(1, 100)
# Define the range of possible guesses
range_min = 1
range_max = 100
current_range = (range_min, range_max)

# Print a message telling the user to guess the number
print(f"I'm thinking of a number between {range_min} and {range_max}. Can you guess what it is?")

# Loop until the user guesses the correct number
attempts = 0
while True:
    # Ask the user to guess the number
    guess = int(input("Enter your guess: "))
    attempts += 1
    # Check if the guess is correct
    if guess == n:
        print(f"Congratulations, you guessed the number in {attempts} attempts!")
        break
    elif guess < n:
        print("Too low! Try again.")
        # Update the range of possible guesses
        current_range = (guess + 1, current_range[1])
    else:
        print("Too high! Try again.")
        # Update the range of possible guesses
        current_range = (current_range[0], guess - 1)

    # If the user has made 3 consecutive incorrect guesses, give a hint
    if attempts % 3 == 0:
        midpoint = (current_range[0] + current_range[1]) // 2
        print(f"Hint: the number is between {midpoint - midpoint//2} and {midpoint + midpoint//2}")
