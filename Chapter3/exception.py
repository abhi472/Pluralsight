student = {
    "name": "mark",
    "student_id": 123,
    "feedback": None
}

try:                                              # exception handling with try-except block
    last_name = student["last_name"]
except KeyError:
    print("Error : last_name Doesn't exist")




