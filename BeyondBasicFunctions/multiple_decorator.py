class decorator_class:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        x = self.f(*args, **kwargs)
        self.count += 1
        return x

def escape_unicode(f):
    def wrap(y):
        x  = f(y) + "acb"
        return x
    return wrap


@decorator_class
@escape_unicode
def print_val(x):
    return x