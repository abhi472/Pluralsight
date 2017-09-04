# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
import time, math


def isPrime(i):
    if i == 2 or i == 3:
        return True
    else:
        if (i % 2) == 0:
            return False
        else:
            for j in range(2, int(i/2)):
                if (i % j) == 0:
                    return False
    return True

def n_prime(x):
    i = 3
    count = 1
    while(True):
        if(isPrime(i)):
            count += 1
            if(count == x):
                return i
        i += 2

start = time.time()
print(n_prime(10001))
delay = time.time() - start
print(delay)
