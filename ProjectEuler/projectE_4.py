# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
#  numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
import time

def isPalin(x):
    if (type(x) != str):
        x = str(x)
    list_num = list(x)
    if (len(list_num) != 1):
        while (len(list_num) > 0):
            if (list_num[0] == list_num[-1]):
                if (len(list_num) != 1):
                    list_num.remove(list_num[0])
                    list_num.remove(list_num[-1])
                else:
                    break
            else:
                return False
    else:
        return "single digit numbers can't be palindromes"
    return True

def isPalin2(num):
    if str(num)==str(num)[::-1]: return True
    else: return False


def isPalin3(num):
    reversed = 0
    original = num

    if num < 10: return True
    if num % 10 == 0: return False

    while num >= 1:
        reversed = (reversed * 10) + (num % 10)
        num = num / 10

    if original == reversed:
        return True
    else:
        return False


start = time.time()
for i in range(10000000, 10000002): # my palindrome logic is more efficient
    a =isPalin(i)
elapsed = time.time() - start

print(elapsed)


start = time.time()
for i in range(10000000, 10000002): # my palindrome logic is more efficient in case of larger numbers
    a =isPalin2(i)
elapsed = time.time() - start

print(elapsed)













