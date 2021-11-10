# Prime Numbers Calculator - Python
# Hayden Brown
import time

startTime = time.perf_counter()

limit = int(input("Enter maximum number: "))

primes = []

def factors(n):
    f = []
    for i in range(1, n + 1):
        if n % i == 0:
            f.append(i)
    return f

print("Calculating prime numbers...")

for i in range(1, limit + 1):
    if len(factors(i)) <= 2 and i != 1:
        primes.append(i)
        print(i)

endTime = time.perf_counter()
print("Time taken: " + str(round(endTime - startTime, 2)) + "s")
