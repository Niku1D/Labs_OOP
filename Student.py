class Student:
    def __init__(self, id, name, faculty, email=None):
        self.id = id
        self.name = name
        self.faculty = faculty
        self.email = email
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        course.enrolledStudents.append(self)

    def to_string(self):
        return f"{self.id},{self.name},{self.faculty.id},{self.email}"