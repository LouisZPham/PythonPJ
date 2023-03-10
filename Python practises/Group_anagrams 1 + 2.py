def findMissingNumbers(n):
    # Create a set of all the numbers in the input list
    numbers = set(n)
    # Get the length of the input list
    length = len(n)
    # Create an empty list to store the missing numbers
    output = []
    
    # Iterate over the range of numbers from 1 to the second-to-last number in the input list
    for i in range(1, n[-1]):
        # If the current number is not in the set of numbers from the input list, it is missing
        if i not in numbers:
            # Append the missing number to the output list
            output.append(i)
    return output
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))