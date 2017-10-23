from time import time

#  a function to display usage of non local, this function basically mimics the

def get_elapsed_time():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed



