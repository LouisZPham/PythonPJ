import time
import timeit

#Use time to check execution_time
start = time.perf_counter()

# Python program to create acronyms
word = "Trying to loop more to check"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time.perf_counter()
execution_time = end - start
print("Execution Time : {:.10f}".format(execution_time))

#use timeit to check time loop
t1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print("Time taken using timeit: {:.10f}".format(t1))

t2 = timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
print("Time taken using lambda: {:.10f}".format(t2))
