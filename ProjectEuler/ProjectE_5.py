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

# def getPrimeFactors(x):
#     for i in range(2, int(x/2)):
#         if(x == 1):
#             break
#         else :
#             while(x % i == 0):

def get_smallest_evenly_divisible(x):
    primeProduct = 1
    listNum = []
    listComposite = []
    for i in range(2, x):
        if (isPrime(i)):
            primeProduct *= i
            listNum.append(i)
        else :
            for k in listNum:
                if((math.log(i,k).is_integer())) :
                    primeProduct *= k
                    break
            listComposite.append(i)
    return primeProduct






print(get_smallest_evenly_divisible(30))

