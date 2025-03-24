import os
import time
from models.student import Student
from repository.student_repository import *
from utils.consts import TIME_SLEEP, BINARY_PATH
from utils.validators import validate_integer_value


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def remove_file():
    if (os.path.isfile(BINARY_PATH)):
        os.remove(BINARY_PATH)


def show_continue():
    input("\nPressione qualquer tecla para continuar")


def show_students(students: []):
    if (len(students) == 0):
        print("\nNenhum aluno cadastrado")
    else:
        for student in students:
            print(student)


def show_student(student: Student | None):
    if (student == None):
        print("\nAluno não encontrado")
    else:
        print(student)


def show_options():
    print("\nMenu:")
    print("1. Adicionar aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno por ID")
    print("4. Atualizar notas do aluno ")
    print("5. Excluir aluno")
    print("0. Sair")


def input_student() -> Student:
    student = Student()
    student.input_name()
    student.input_registration()
    student.input_gradeA()
    student.input_gradeB()
    student.input_gradeC()
    return student


def update_student(student: Student) -> Student:
    student.input_gradeA()
    student.input_gradeB()
    student.input_gradeC()
    return student


def input_id() -> int:
    while True:
        user_input = input("Informe o ID do aluno: ")
        try:
            return validate_integer_value(user_input, 4, 0, 9999)
        except ValueError as e:
            print(e.args[0])


def handle_option(user_input):
    try:
        option = int(user_input)
    except:
        print("Entrada inválida!")
        time.sleep(TIME_SLEEP)
        return

    match option:
        case 1:
            student = input_student()
            insert_student(student)
            print(f"Aluno adicionado com sucesso:\n{student}")
            show_continue()
        case 2:
            students = find_all_students()
            show_students(students)
            show_continue()
        case 3:
            student = find_student_by_id(input_id())
            show_student(student)
            show_continue()
        case 4:
            student_id = input_id()
            student = find_student_by_id(student_id)
            if (student == None):
                print("\nAluno não encontrado")
            else:
                student = update_student(student)
                remove_student(student_id)
                insert_student(student)
                sort_file()
                print(f"Aluno atualizado com sucesso:\n{student}")
            show_continue()
        case 5:
            student_id = input_id()
            student = find_student_by_id(student_id)
            if (student == None):
                print("\nAluno não encontrado")
            else:
                remove_student(student_id)
                print(f"Aluno removido com sucesso!")
            show_continue()
        case 0:
            print("\nEncerrando ...")
            time.sleep(TIME_SLEEP)
            clear()
            exit()
        case _:
            print("\nOpção inválida!")
            time.sleep(TIME_SLEEP)


def main():
    while True:
        clear()
        show_options()
        handle_option(input("Escolha uma opção: "))


if __name__ == "__main__":
    clear()
    remove_file()
    main()
