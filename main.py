from FileManager import FileManager
from University import University
from Faculty import Faculty
from Student import Student
from Course import Course

if __name__ == "__main__":
    # file_manager = FileManager()
    # faculties = file_manager.read_faculties_from_file()
    #
    # for faculty in faculties:
    #     print(faculty.to_string())
    #
    # students = file_manager.get_students_from_file()
    #
    # for student in students:
    #     print(student.to_string())

    tum = University("Technical University of Moldova")

    faculty_cs = Faculty(1, "Computer Science")
    faculty_it = Faculty(2, "Information Technology")

    tum.add_faculty(faculty_cs)
    tum.add_faculty(faculty_it)

    student1 = Student("001", "Ion Popescu", faculty_cs, "ion@tum.md")
    student2 = Student("002", "Maria Ionescu", faculty_cs, "maria@tum.md")
    student3 = Student("003", "Nicu Nicolae", faculty_it, "nicu@tum.md")
    student4 = Student("004", "Daniela Duca", faculty_it, "daniela@tum.md")

    faculty_cs.add_student(student1)
    faculty_cs.add_student(student2)
    faculty_it.add_student(student3)
    faculty_it.add_student(student4)

    faculty_it.graduate_student(student1)
    faculty_cs.graduate_student(student2)

    faculty_it.display_current_students()

    faculty_cs.display_current_students()
    faculty_cs.display_graduates()

    if faculty_cs.is_student_in_faculty(student1):
        print(f"{student1.name} belongs to {faculty_cs.name}")

    found_faculty = tum.search_faculty_by_student("002")
    if found_faculty:
        print(f"Student found in faculty: {found_faculty.name}")

    tum.display_all_faculties()

    tum.display_faculties_by_field("Computer")

    print("-" * 20)

    file_manager = FileManager()
    students = tum.get_all_students()
    faculties = tum.faculties

    file_manager.save_students_to_file(students)
    file_manager.save_faculties_to_file(faculties)
