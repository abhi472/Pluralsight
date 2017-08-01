a = [1, 2, 3]
b = a

a[1] = 17  # both a and b are changed because both of them are pointing to [1, 2, 3] which in itself is an object

print(a)
print(b)
print(a is b)


c = 6

d = c

c = 7

print(c)
print(d)
print(c is d)


e = 5
f = 5

print(id(e))
print(id(f))
print(e is f)

g = "hey jude"
h = "hey jude"

print(id(g))
print(id(h))
print(g is h)


i = [1, 5, 7]    # here id(i) != id(j)
j = [1, 5, 7]    # imp ! imp ! imp !

print(id(i))
print(id(j))
print(i is j)


k = 'a'
l = "a"
m = "a"

print(id(k))
print(id(l))
print(id(m))