# Prime Numbers Calculator - Python
# Hayden Brown
import time

startTime = time.perf_counter()

limit = int(input("Enter maximum number (-1 for infinite): "))
listPrimes = False

primes = []

def factors(n):
    f = []
    for i in range(1, n + 1):
        if n % i == 0:
            f.append(i)
    return f

print("Calculating prime numbers...")

if limit == -1:
    i = 1
    while True:
        if len(factors(i)) <= 2 and i != 1:
            primes.append(i)
            if listPrimes:
                print(i)
        i = i + 1
else:
    for i in range(1, limit + 1):
        if len(factors(i)) <= 2 and i != 1:
            primes.append(i)
            if listPrimes:
                print(i)

endTime = time.perf_counter()
print("Time taken: " + str(round(endTime - startTime, 2)) + "s")
