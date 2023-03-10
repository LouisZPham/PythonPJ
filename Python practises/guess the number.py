import random
#Guess the number with hint that will reduce range by half every 3 times failed in guessing.
n = random.randrange(1,100)
guess = int(input("Enter any number between 1 to 100: "))
attempts = 1
while n!= guess:
    if attempts % 3 == 0:
        n = random.randrange(n//2,100) # reduce the range by half
        print("Hint: the number is between", n, "and 10")
    if guess < n:
        print("Too low")
        guess = int(input("Enter another one please: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter another one please: "))
    else:
      break
    attempts += 1
print("you guessed it right in", attempts, "attempts!")