def var_args(name, *args):
    print(name)
    for names in args:
        print(names)


def kw_args(name, **kwargs):
    print(name)
    print(kwargs["desc"])
    print(kwargs["surname"])
    print(kwargs["age"])
    print(kwargs["occupation"])


var_args("abhishek", "android", "python", "CSharp", True)  # using variable number of arguments

kw_args("abhishek", desc="yo", surname="tiwari", age=22, occupation="Android Dev") # using kwargs
