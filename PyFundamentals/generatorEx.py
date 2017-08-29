def take(count, iterable):
    counter = 0
    for i in iterable:
        if counter == count:
            return
        counter += 1
        yield i

def run_take():
    items = [1,2,4,6,8,9]
    for i in take(3, items):
        print(i)


if __name__ == '__main__':
    run_take()