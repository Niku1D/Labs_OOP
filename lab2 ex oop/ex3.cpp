#include <iostream>
#include <string>

using namespace std;

class Person {
public:
    virtual string getRole() const = 0;
    virtual ~Person() {}             
};

class Student : public Person {
public:
    string getRole() const override {
        return "Student";
    }
};

class Teacher : public Person {
public:
    string getRole() const override {
        return "Teacher";
    }
};

class Administrator : public Person {
public:
    string getRole() const override {
        return "Administrator";
    }
};

int main() {
    Person* student = new Student();
    Person* teacher = new Teacher();
    Person* admin = new Administrator();

    cout << "Role: " << student->getRole() << endl;
    cout << "Role: " << teacher->getRole() << endl;
    cout << "Role: " << admin->getRole() << endl;

    delete student;
    delete teacher;
    delete admin;

    return 0;
}
