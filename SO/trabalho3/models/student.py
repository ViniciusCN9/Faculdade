from utils.validators import validate_integer_value, validate_string_value


class Student():
    ID = 1

    def __init__(self, id=None, name="", registration="", gradeA="0", gradeB="0", gradeC="0"):
        self.name = name.ljust(30)
        self.registration = registration.ljust(11)
        self.gradeA = gradeA.zfill(3)
        self.gradeB = gradeB.zfill(3)
        self.gradeC = gradeC.zfill(3)
        if (id == None):
            self.id = str(Student.ID).zfill(4)
            Student.ID = Student.ID + 1
        else:
            self.id = id

    def __str__(self):
        return f"Id: {self.id} | Nome: {self.name} | Matrícula: {self.registration} | Nota A: {self.gradeA} | Nota B: {self.gradeB} | Nota C: {self.gradeC}"

    def input_name(self):
        while True:
            user_input = input("Informe o nome do aluno: ")
            try:
                self.name = validate_string_value(user_input, 30)
                return
            except ValueError as e:
                print(e.args[0])

    def input_registration(self):
        while True:
            user_input = input("Informe a matrícula do aluno: ")
            try:
                self.registration = validate_string_value(user_input, 11)
                return
            except ValueError as e:
                print(e.args[0])

    def input_gradeA(self):
        while True:
            user_input = input("Informe a nota A do aluno: ")
            try:
                self.gradeA = validate_integer_value(user_input, 3, 0, 100)
                return
            except ValueError as e:
                print(e.args[0])

    def input_gradeB(self):
        while True:
            user_input = input("Informe a nota B do aluno: ")
            try:
                self.gradeB = validate_integer_value(user_input, 3, 0, 100)
                return
            except ValueError as e:
                print(e.args[0])

    def input_gradeC(self):
        while True:
            user_input = input("Informe a nota C do aluno: ")
            try:
                self.gradeC = validate_integer_value(user_input, 3, 0, 100)
                return
            except ValueError as e:
                print(e.args[0])
