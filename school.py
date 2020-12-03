class Groupp:
    def __init__(self):
        self.students = []
        file2 = open('data.txt', 'w+')
        file2.readlines()
        spisok = []
        for self.students in file2:


    def add_student(self, student_name):
        self.students.append(student_name)

    def show_students(self):
        # for i in range(len(self.students)):
        #     print(self.students[i])
        print('/n'.join(self.students))

    def remove_student(self, student_name):
        self.students.remove(student_name)

    def save_students(self):
        file = open('data.txt', 'w+')
        file.readlines()
        for i in self.students:
            file.write(i + '\n')

B8 = Groupp()
while True:
    k = int(input())
    if k == 1:
        B8.add_student(input())
    if k == 2:
        B8.remove_student(input())
    if k == 3:
        B8.show_students()
    if k == 4:
        B8.save_students()
