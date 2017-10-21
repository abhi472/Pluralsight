import math

def pro_E6(x):
    a = (math.pow(x,4) + math.pow(x,2) + 2*math.pow(x,3))/4
    b = (2*math.pow(x,3) + 3*math.pow(x,2) + x)/6
    return a-b

print(pro_E6(100))