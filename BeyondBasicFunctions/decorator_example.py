def escape_unicode(f):
    def wrap(y):
        x  = f(y) + "acb"
        return x
    return wrap

@escape_unicode
def func(x):
    return x