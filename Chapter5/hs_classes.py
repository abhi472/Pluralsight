from Chapter5.classes import Student


class HighSchoolStudent(Student):

    school_name = "SMJPS Jr."

    def get_school_name(self):
        return self.school_name

    def get_super_school_name(self):
        original_school =  super().get_school_name
        return original_school
