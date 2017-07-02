student = []


def student_name_list():
    student_first_name = []
    for name in student:
        student_first_name = name.title
    return student_first_name


def print_student_name_list():
    student_first_name = student_name_list()
    print(student_first_name)


def add_student(name):
    student.append(name)


add_student("abhishek")
add_student("vivek")
add_student("anubhav")
add_student("random")


print_student_name_list()


