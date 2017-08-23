list = ['a','b','c','d','e']

full_list = list[: ]

print(full_list is list)
print(list)
print(full_list)

list[4] = 'f'

print(list)
print(full_list)

list.append('g')

print(list)
print(full_list)

list2 = [1]
list2 = list2 *5

list2.remove(1)

print(list2)