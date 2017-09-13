# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc


# trick here is that pythagorean triplets follow this sequence
# a, b, c are pyhtagorean triplet if
# a = n^2 - m^2
# b = 2nm
# c = n^2 + m^2, so abc = 2^(n^5*m - m^5*n)

import time

def calculator(n):

    n= n/2
    for i in range(2, int( n** .5)):
        for j in range(1, i):
            if ((i ** 2 + i * j) == n):
                return i, j
            else:
                if((i ** 2 + i * j) > n):
                    break

start = time.time()
a, b = calculator(1000)
print(2*(((a**5)*b)-((b**5)*a)))
print(time.time() - start)