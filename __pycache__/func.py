def get_student_names(students):
    a = sorted(students.values())
    return a
students = {1: "Rhaeny", 2: "Dana", 3: "Vhagar"}
b = get_student_names(students)
print(b)

