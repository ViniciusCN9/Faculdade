import struct
from models.student import Student
from utils.consts import BINARY_PATH, STUDENT_REGISTRY_SIZE, STUDENT_REGISTRY_FORMAT


def insert_student(student: Student):
    with open(BINARY_PATH, "a+b") as file:
        data = struct.pack(STUDENT_REGISTRY_FORMAT,
                           student.id.encode(),
                           student.name.encode(),
                           student.registration.encode(),
                           student.gradeA.encode(),
                           student.gradeB.encode(),
                           student.gradeC.encode())
        file.seek(0, 2)
        file.write(data)


def find_all_students() -> []:
    with open(BINARY_PATH, "a+b") as file:
        students = []
        file.seek(0)
        while True:
            data = file.read(STUDENT_REGISTRY_SIZE)
            if not data:
                break

            student = Student(1)
            student.id, student.name, student.registration, student.gradeA, student.gradeB, student.gradeC = struct.unpack(
                STUDENT_REGISTRY_FORMAT, data)
            student = decode_attributes(student)
            students.append(student)
        return students


def find_student_by_id(id: str) -> Student:
    with open(BINARY_PATH, "a+b") as file:
        file.seek(0)
        while True:
            data = file.read(STUDENT_REGISTRY_SIZE)
            if not data:
                break

            student = Student(1)
            student.id, student.name, student.registration, student.gradeA, student.gradeB, student.gradeC = struct.unpack(
                STUDENT_REGISTRY_FORMAT, data)
            student = decode_attributes(student)

            if (student.id == id):
                return student
        return None


def remove_student(id: str):
    new_data = []
    with open(BINARY_PATH, "a+b") as file:
        file.seek(0)
        while True:
            old_data = file.read(STUDENT_REGISTRY_SIZE)
            if not old_data:
                break

            student = Student(1)
            student.id, student.name, student.registration, student.gradeA, student.gradeB, student.gradeC = struct.unpack(
                STUDENT_REGISTRY_FORMAT, old_data)
            student = decode_attributes(student)

            if (student.id != id):
                new_data.append(old_data)

        file.seek(0)
        file.truncate(0)
        for data in new_data:
            file.write(data)
        return None


def sort_file():
    new_data = []
    with open(BINARY_PATH, "a+b") as file:
        file.seek(0)
        while True:
            old_data = file.read(STUDENT_REGISTRY_SIZE)
            if not old_data:
                break
            new_data.append(old_data)

        new_data.sort()
        file.seek(0)
        file.truncate(0)
        for data in new_data:
            file.write(data)
        return None


def decode_attributes(student: Student) -> Student:
    student.id = student.id.decode()
    student.name = student.name.decode()
    student.registration = student.registration.decode()
    student.gradeA = student.gradeA.decode()
    student.gradeB = student.gradeB.decode()
    student.gradeC = student.gradeC.decode()
    return student
