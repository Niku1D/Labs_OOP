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

void printRole(const Person* person) {
    cout << "Role: " << person->getRole() << endl;
}

int main() {
    Person* student = new Student();
    Person* teacher = new Teacher();

    printRole(student);
    printRole(teacher); 

    delete student;
    delete teacher;

    return 0;
}
