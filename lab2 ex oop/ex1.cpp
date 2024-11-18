#include <iostream>
using namespace std;

class Student {
private:
    int credits;

public:

    Student(int c = 0) : credits(c) {}

    int getCredits() const { return credits; }

    Student operator++(int) {
        Student temp = *this;
        credits++;
        return temp;
    }

    Student operator--(int) {
        Student temp = *this;
        credits--;
        return temp;
    }

    Student& operator+=(const Student& other) {
        credits += other.credits;
        return *this;
    }

    Student operator+(const Student& other) const {
        return Student(credits + other.credits);
    }

    void display() const {
        cout << "Credits: " << credits << endl;
    }
};

int main() {
    Student s1(10), s2(15);

    cout << "Original Credits:" << endl;
    s1.display();
   
    s1++;
    cout << "After ++ (postfix):" << endl;
    s1.display();

    s1--;
    cout << "After -- (postfix):" << endl;
    s1.display();

    s1 += s2;
    cout << "After s1 += s2:" << endl;
    s1.display();

    Student s3 = s1 + s2;
    cout << "After s3 = s1 + s2:" << endl;
    s3.display();

    return 0;
}
