class Faculty:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.departments = []
        self.students = []
        self.graduates = []
    

    def add_student(self, student):
        self.students.append(student)

 
    def graduate_student(self, student):
        if student in self.students:
            self.students.remove(student)
            self.graduates.append(student)
    
  
    def display_current_students(self):
        print("Current Students in Faculty:", self.name)
        for student in self.students:
            print(student.name)
    
    
    def display_graduates(self):
        print("Graduates of Faculty:", self.name)
        for graduate in self.graduates:
            print(graduate.name)
    
    def is_student_in_faculty(self, student):
        return student in self.students or student in self.graduates

    def to_string(self):
        return f"{self.id},{self.name}"
