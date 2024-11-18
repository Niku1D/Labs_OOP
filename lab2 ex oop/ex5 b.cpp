#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Book {
public:
    Book(const string& title) : title(title) {}
    string getTitle() const {
        return title;
    }
private:
    string title;
};

class Library {
public:
    Library(const string& name) : name(name) {}

    void addBook(const string& bookTitle) {
        books.push_back(new Book(bookTitle));
    }

    void printBooks() const {
        cout << "Library: " << name << endl;
        cout << "Books: " << endl;
        for (const auto& book : books) {
            cout << "- " << book->getTitle() << endl;
        }
    }

    ~Library() {
        for (auto book : books) {
            delete book; 
        }
    }

private:
    string name;
    vector<Book*> books; 
};

int main() {
    Library library("City Library");
    
    library.addBook("C++ Programming");
    library.addBook("Design Patterns");
    
    library.printBooks();
    
    return 0;
}
