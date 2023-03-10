# Mean
list1 = [1, 14, 25, 20, 12, 32, 52, 21, 124, 42]
mean = sum(list1)/len(list1)
print(mean)

#Median

list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)