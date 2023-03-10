#Create a list that groups all the elements with same index into lists in a list
givenLists = [[10, 30, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []
index = 0
for i in range(len(givenLists[1])):
    outputLists.append([])
    for j in range(len(givenLists)):
    # Append the element at the current index of the current sublist to the output list
        outputLists[index].append(givenLists[j][index])
    index = index + 1

# Unpack the output list into separate variables
a, b, c = outputLists[0], outputLists[1], outputLists[2]

print(a, b, c)