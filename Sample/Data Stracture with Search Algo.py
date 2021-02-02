# region class Classlist
class Class_list:
    def __init__(self):
        print("New class has been INSTANTIATED")
        self.student_list = list()
        self.number_of_student = 0

    def set_number_of_student(self):
        self.number_of_student = int(input("How many students for this class?"))

    def show_all_students(self):
        student_count = 1
        for student in self.student_list:
            print("Student No.",student_count,"'s Info are the following: ")
            student.show_student_info()
            student_count += 1

    def search_student_linear(self):
        name = input("Input name of student to be search")
        for student in self.student_list:
            if name == student.get_student_name():
                print("Search Successful")
                student.show_student_info()

    def add_student(self):
        student = Student()
        student.set_student_info()
        self.student_list.append(student)

    def class_list_menu(self):
        self.operation = int(input("What to do next?"))
        if self.operation == 1:
            self.show_all_students()
        elif self.operation == 2:
            self.search_student_linear()

    def set_students(self):
        for iteration in range(class_list.number_of_student):
            class_list.add_student()




# endregion

# region class Student
class Student:
    def __init__(self):
        print("New Student has been INSTANTIATED")
        self.student_name = "default name"
        self.student_number = "default student number"
        self.student_program = "default program"

    def set_student_name(self):
        self.student_name = input("Enter Student Name: ")

    def get_student_name(self):
        return self.student_name

    def set_student_number(self):
        self.student_number = input("Enter Student Number: ")

    def set_student_program(self):
        self.student_program = input("Enter Student program: ")

    def set_student_info(self):
        self.student_name = input("Enter Student Name: ")
        self.student_number = input("Enter Student Number: ")
        self.student_program = input("Enter Student program: ")

    def show_student_info(self):
        print("\tStudent Name: ", self.student_name, end="\t")
        print("Student Number: ", self.student_number, end="\t")
        print("Student Program: ", self.student_program)




# endregion

if __name__ == "__main__":
    class_list = Class_list()
    class_list.set_number_of_student()
    class_list.set_students()
    class_list.class_list_menu()
00
