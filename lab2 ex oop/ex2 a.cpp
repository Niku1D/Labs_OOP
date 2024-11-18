#include <iostream>
#include <string>
using namespace std;

class Person {
protected:
    string name;
    int age;

public:
    Person(string name, int age) : name(name), age(age) {}

    void displayInfo() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

class Student : public Person {
private:
    string studentID;
    string faculty;

public:
    Student(string name, int age, string studentID, string faculty)
        : Person(name, age), studentID(studentID), faculty(faculty) {}

    void displayStudentInfo() {
        displayInfo();
        cout << "Student ID: " << studentID << ", Faculty: " << faculty << endl;
    }
};

int main() {
    Person person("Alice", 45);
    person.displayInfo();

    Student student("Bob", 20, "S12345", "Engineering");
    student.displayStudentInfo();

    return 0;
}
