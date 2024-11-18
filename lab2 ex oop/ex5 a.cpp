#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Student {
public:
    Student(const string& name) : name(name) {}
    string getName() const {
        return name;
    }
private:
    string name;
};

class Faculty {
public:
    Faculty(const string& name) : name(name) {}

    void addStudent(Student* student) {
        students.push_back(student);
    }

    void printStudents() const {
        cout << "Faculty: " << name << endl;
        cout << "Students: " << endl;
        for (const auto& student : students) {
            cout << "- " << student->getName() << endl;
        }
    }

private:
    string name;
    vector<Student*> students;

int main() {
    Student* student1 = new Student("John");
    Student* student2 = new Student("Alice");

    Faculty faculty("Computer");
    
    faculty.addStudent(student1);
    faculty.addStudent(student2);

    faculty.printStudents();

    delete student1;
    delete student2;

    return 0;
}
