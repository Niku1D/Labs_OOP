#include <iostream>
#include <string>

class Person {
protected:
    std::string name;
    int age;

public:
    Person(const std::string& name, int age) : name(name), age(age) {}

    void displayInfo() const {
        std::cout << "Name: " << name << ", Age: " << age << std::endl;
    }
};

class Student : public Person {
protected:
    std::string studentID;
    std::string faculty;

public:
    Student(const std::string& name, int age, const std::string& studentID, const std::string& faculty)
        : Person(name, age), studentID(studentID), faculty(faculty) {}

    void displayStudentInfo() const {
        displayInfo();
        std::cout << "Student ID: " << studentID << ", Faculty: " << faculty << std::endl;
    }
};

class Employee {
protected:
    std::string employeeID;
    std::string position;

public:
    Employee(const std::string& employeeID, const std::string& position)
        : employeeID(employeeID), position(position) {}

    void displayEmployeeInfo() const {
        std::cout << "Employee ID: " << employeeID << ", Position: " << position << std::endl;
    }
};

class StudentEmployee : public Student, public Employee {
public:
    StudentEmployee(const std::string& name, int age, const std::string& studentID, const std::string& faculty,
                    const std::string& employeeID, const std::string& position)
        : Student(name, age, studentID, faculty), Employee(employeeID, position) {}

    void displayFullInfo() const {
        displayStudentInfo();
        displayEmployeeInfo();
    }
};

int main() {
    
    StudentEmployee studentEmployee("Charlie", 25, "S54321", "Business", "E67890", "Intern");
    studentEmployee.displayFullInfo();

    return 0;
}
