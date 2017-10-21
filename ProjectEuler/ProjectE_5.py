import math

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

def get_smallest_evenly_divisible(x):
    primeProduct = 1
    listNum = []
    for i in range(2, x):
        if (isPrime(i)):
            primeProduct *= i
            listNum.append(i)
        else :
            for k in listNum:
                if((math.log(i,k).is_integer())) :
                    primeProduct *= k
                    break
    return primeProduct






print(get_smallest_evenly_divisible(20))

