from Faculty import Faculty
from Student import Student


class FileManager:
    def __init__(self):
        self.student_filename = "students.txt"
        self.faculty_filename = "faculties.txt"

    def save_students_to_file(self, students):
        with open(self.student_filename, "w") as file:
            for student in students:
                file.write(student.to_string() + "\n")
            file.close()

    def save_faculties_to_file(self, faculties):
        with open(self.faculty_filename, "w") as file:
            for faculty in faculties:
                file.write(faculty.to_string() + "\n")
            file.close()

    def get_students_from_file(self):
        faculties = self.read_faculties_from_file()
        students = []

        with open(self.student_filename, "r") as file:
            for student in file:
                student = student.split(",")

                for faculty in faculties:
                    if faculty.id == student[2]:
                        student_faculty = faculty

                s = Student(student[0], student[1], student_faculty, student[3])
                students.append(s)

        return students

    def read_faculties_from_file(self):
        faculties = []
        with open(self.faculty_filename, "r") as file:
            for faculty in file:
                faculty = faculty.split(",")
                f = Faculty(faculty[0], faculty[1])
                faculties.append(f)

        return faculties
