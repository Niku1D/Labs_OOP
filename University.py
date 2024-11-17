class University:
    def __init__(self, name):
        self.name = name
        self.faculties = []

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def search_faculty_by_student(self, student_id):
        for faculty in self.faculties:
            for student in faculty.students + faculty.graduates:
                if student.id == student_id:
                    return faculty
        return None

    def display_all_faculties(self):
        print("Faculties at", self.name)
        for faculty in self.faculties:
            print(faculty.name)

    def display_faculties_by_field(self, field):
        print(f"Faculties related to {field}:")
        for faculty in self.faculties:
            if field.lower() in faculty.name.lower():
                print(faculty.name)

    def get_all_students(self):
        students = []
        for faculty in self.faculties:
            for student in faculty.students:
                students.append(student)

            for student in faculty.graduates:
                students.append(student)

        return students
