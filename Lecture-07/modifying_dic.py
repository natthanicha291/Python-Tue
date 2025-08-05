student = {"name": "Natee", "age": 19, "grade": "A"}

student["age"] = 18
student["major"] = "Computer Science"
print(student)

del student["grade"]
print(student)

remove_major = student.pop("major")
print(remove_major)
print(student)