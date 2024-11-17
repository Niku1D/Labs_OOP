class Course:
    def __init__(self, code, name, professor=None):
        self.courseCode = code
        self.courseName = name
        self.professor = professor
        self.enrolledStudents = []