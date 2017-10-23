def print_args(*args):   #args is a tuple
    print(args)


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(abc=10, xyz=11)   #printing a dict

print_args("hey", "jude", 1, 2, 3)   #printing a tuple