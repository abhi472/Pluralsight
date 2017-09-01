# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math
def largest_prime(i):   # first removing all 2 that are the factors
    lists = []
    while(i%2 == 0):
        i/=2

    for x in range(3,int(math.sqrt(i))):  # starting from 3 to the sqrt of the number we are checking if divisible
        if(i % x == 0):
            lists.append(x)
            i/=x                          # removing a divisor upon iteration so successive iterations take less time


    return lists

print(largest_prime(600851475143)[-1])

