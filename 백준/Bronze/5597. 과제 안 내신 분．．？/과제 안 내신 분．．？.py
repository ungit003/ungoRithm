students = list(range(1, 31))
subjects = list()
for i in range(28):
    subjects.append(int(input()))
for student in students:
    if student not in subjects:
        print(student)