x = 0
for index in range(10):  # here range creates a list of size 10(argument that has been passed)
    x += 10
    print("The value of X is {0}".format(x))

for index in range(5, 10):  # two args mean list start from 5 and goes till 9
    x += 10
    print("The value of X is {0}".format(x))

for index in range(5, 10, 2):  # three args mean list start from 5 and increments two till 9
    x += 10
    print("The value of X is {0}".format(x))