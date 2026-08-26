# student1_name = "Aisha"
# student1_gpa = 3.8
 
# student2_name = "Diego"
# student2_gpa = 3.2
 
# def print_student(name, gpa):
#     print(f"{name}: GPA {gpa}")
 
# print_student(student1_name, student1_gpa)
# print_student(student2_name, student2_gpa)
 
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

students = [
    Student('Aisha', 3.2),
    Student('Diego', 3.8),
    Student('Steve', 1.5)
]

avg = 0.0
total = 0.0
for s in students:
    total += s.gpa

print(f'The average is {total/len(students):.2f}')


# s1 = Student('Aisha',3.8)
# s2 = Student('Diego',3.2)

# print(f'Name: {s1.name} Gpa: {s1.gpa}')
# print(f'Name: {s2.name} Gpa: {s2.gpa}')