def enter_elements(n):
    lists = []
    for i in range(n):
        lists.append(i)
    return tuple(lists)

def minmax():
    return min(tuple), max(tuple)


a = input("enter number of elements")
tuple = enter_elements(int(a))
print(minmax())