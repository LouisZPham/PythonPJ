from time import time
import timeit
#Use time to check execution_time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)
#use timeit to check time loop
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
