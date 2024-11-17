class LoggingSystem():
    instance = None
    filename = 'log.txt'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoggingSystem, cls).__new__(cls)
        return cls.instance

    def log_student_graduation(self, student):
        with open(self.filename, 'w') as file:
            file.write(f"Student with id {student.id}, has been graduated.\n")
        file.close()

    def log_student_creation(self, student):
        with open(self.filename, 'w') as file:
            file.write(f"Student with id {student.id}, has been created.\n")
        file.close()

    def log_faculty_creation(self, faculty):
        with open(self.filename, 'w') as file:
            file.write(f"Faculty with id {faculty.id}, has been created.\n")
        file.close()
