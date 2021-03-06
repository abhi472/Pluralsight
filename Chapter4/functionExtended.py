students = []


def student_name_list():
    student_first_name = []
    for name in students:
        student_first_name.append(name) # appending a list with a dict
    return student_first_name


def print_student_name_list():
    student_first_name = student_name_list()
    print(student_first_name)


def add_student(name):
    students.append(name)


def add_student_dict(name, student_id):
    student = {"name": name,
               "student_id": student_id
               }
    students.append(student)              # appending a dict to student


def print_student(name, student_id=322):  # student_id = 322 means that we are setting a default value to student id
    print("name is {0} and id is {1}".format(name, student_id))


add_student("abhishek")
add_student("vivek")
add_student("anubhav")
add_student("random")
print_student("name", 10)  # passed argument taken
print_student("name2")  # default value taken
add_student_dict("abhishek2", 10)
print_student_name_list()
