def check_non_negative(index):
    def validator(f):               # the actual decorator here is validator and not check_non_negative
        def wrap(*args):
            if args[index]< 0:
                raise ValueError(
                    'Argument cannot be non-negative'
                )
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)             # check_non_negative(index) returns a function here which is defined as validator in check_non_negative and that acts as a decorator here
def string_multiplier(val, times):
    return val * times