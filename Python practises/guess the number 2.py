import random
#Guess the number 3. Range will reduce by half continously with every 3 times failed in guessin.
n = random.randrange(1, 100)
original_range = (1, 100)
current_range = original_range
guess = int(input("Enter any number between 1 to 100: "))
attempts = 1
consecutive_failures = 0
while n != guess:
    if consecutive_failures == 3:
        current_range = (current_range[0] + (current_range[1] - current_range[0]) // 2, current_range[1])
        print("Hint: the number is between", current_range[0], "and", current_range[1])
        consecutive_failures = 0
    elif consecutive_failures == 6:
        current_range = (current_range[0] + (current_range[1] - current_range[0]) // 2, current_range[1])
        print("Hint: the number is between", current_range[0], "and", current_range[1])
        consecutive_failures = 0
    elif guess < n:
        print("Too low")
        guess = int(input("Enter another one please: "))
        consecutive_failures += 1
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter another one please: "))
        consecutive_failures += 1
    attempts += 1
print("you guessed it right in", attempts, "attempts!")