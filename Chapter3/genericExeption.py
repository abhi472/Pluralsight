student = {
    "name": "mark",
    "student_id": 123,
    "feedback": None,
    "last_name": "Hamill"                         # student["last_name"] = "Hamill" could've also worked
}


try:                                              # exception handling with try-except block
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error : last_name Doesn't exist")
except TypeError as error:                        # generic exception handling
    print(error)
