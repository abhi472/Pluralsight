class decorator_class:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        x = self.f(*args, **kwargs)
        self.count += 1
        return x


@decorator_class
def hello(name):
    return name
