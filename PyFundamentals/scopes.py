count = 0

def show_count():
    print("count = ",count)

def set_count(c):
    global count
    count = c


set_count(5)
show_count()