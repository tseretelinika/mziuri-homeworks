class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_info(self):
        print(f"{self.first_name} {self.last_name}")



class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []


    def add_student(self, student):
        self.students.append(student)


    def remove_student(self, index):
        if 0 <= index < len(self.students):
            self.students.pop(index)
        else:
            print("icorect index")


    def show_students(self):
        for student in self.students:
            student.get_info()




school1 = School("192 skola", "digomi")

student1 = Student("Nika", "Beridze", 15)
student2 = Student("Luka", "Giorgadze", 16)
student3 = Student("Ana", "Melikidze", 15)


school1.add_student(student1)
school1.add_student(student2)
school1.add_student(student3)


print("სკოლის სტუდენტები:")
school1.show_students()


school1.remove_student(1)

print("წაშლის შემდეგ:")
school1.show_students()