#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Base class
class OperationLogger {
public:
    virtual void log(const string& message) = 0;
    virtual ~OperationLogger() {}
};

class FileLogger : public OperationLogger {
public:
    void log(const string& message) override {
       
        ofstream file("log.txt", ios::app); 
        if (file.is_open()) {
            file << message << endl;
            file.close();
        } else {
            cerr << "Unable to open file for logging" << endl;
        }
    }
};

class ConsoleLogger : public OperationLogger {
public:
    void log(const string& message) override {
       
        cout << "Console Log: " << message << endl;
    }
};


void performLogging(OperationLogger* logger, const string& message) {
    logger->log(message); 
}

int main() {
  
    OperationLogger* fileLogger = new FileLogger();
    OperationLogger* consoleLogger = new ConsoleLogger();
 
    performLogging(fileLogger, "File log entry: Operation started.");
    performLogging(consoleLogger, "Console log entry: Operation started.");
    
    delete fileLogger;
    delete consoleLogger;

    return 0;
}
