#include <iostream>
#include <exception>
#include <string>
#include <vector>

using namespace std;

// Base class for custom exceptions (optional, can be omitted if not needed)
class CustomException : public exception {
public:
    virtual const char* what() const noexcept override {
        return "A custom exception occurred";
    }
};

// Custom exception for student not found
class StudentNotFoundException : public CustomException {
public:
    const char* what() const noexcept override {
        return "Student not found in the database.";
    }
};

// Custom exception for invalid faculty operation
class InvalidFacultyOperation : public CustomException {
public:
    const char* what() const noexcept override {
        return "Invalid operation attempted on the faculty.";
    }
};

// Student class
class Student {
public:
    Student(const string& name, int id) : name(name), id(id) {}
    string getName() const {
        return name;
    }
    int getId() const {
        return id;
    }

private:
    string name;
    int id;
};


class Faculty {
public:
    Faculty(const string& name) : name(name) {}

    void addStudent(const Student& student) {
        students.push_back(student);
    }

    Student getStudentById(int id) {
        for (const auto& student : students) {
            if (student.getId() == id) {
                return student;
            }
        }
        throw StudentNotFoundException();
    }

    void performFacultyOperation(bool validOperation) {
        if (!validOperation) {
            throw InvalidFacultyOperation();
        }
        cout << "Faculty operation performed successfully." << endl;
    }

private:
    string name;
    vector<Student> students;
};

int main() {
    try {
        Faculty faculty("Dr. Smith");

        faculty.addStudent(Student("John", 1));
        faculty.addStudent(Student("Alice", 2));

        cout << "Searching for student with ID 3..." << endl;
        Student student = faculty.getStudentById(3);
        cout << "Found student: " << student.getName() << endl;

    } catch (const StudentNotFoundException& e) {
        cout << "Error: " << e.what() << endl;
    } catch (const InvalidFacultyOperation& e) {
        cout << "Error: " << e.what() << endl;
    } catch (const exception& e) {
        cout << "An unexpected error occurred: " << e.what() << endl;
    }

    try {
        Faculty faculty("Dr. Smith");

        faculty.performFacultyOperation(false);  
    } catch (const InvalidFacultyOperation& e) {
        cout << "Error: " << e.what() << endl;
    }

    return 0;
}
