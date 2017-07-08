students = []

class Student:
    school_name = "Sumermal Jain Public School"  # this is similar to a static variable but unlike java we do not need to have a static class for static variables we
                                                 # can have a class instance just like school_name for static call of it

    def __init__(self, name, student_id = 112):
        self.name = name                        # self is an equivalent of this
        self.student_id = student_id            # both self.name and self.student are member variables known as instance variables in python
        students.append(self)


    def __str__(self):                         # overriding
        return "student : " + self.name


    def get_school_name(self):
        return self.school_name


# mark = Student("mark")
# print(mark)
#
# print(Student.school_name)
#
# Student.school_name = "wowo"
#
# print(Student.school_name)
#
# print(mark.get_school_name())  # as expected the school_name will have the same value across all class objects
