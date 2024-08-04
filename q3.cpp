#include <iostream>
#include <string>
using namespace std;

string shiftRightBy13(string message) {
    string encrypted_message = "";

    for (char& c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            c = (c - base + 13) % 26 + base;
        }
        encrypted_message += c;
    }

    return encrypted_message;
}

int getDoubleKeyShiftValue(string key1, string key2) {
    int count = 0;
    
    for (char c1 : key1) {
        for (char c2 : key2) {
            if (c1 == c2) {
                count++;
                break;
            }
        }
    }
    
    return count;
}

string getLayer1MessageEncryption(string message, int method_choice, string key1, string key2) {
    if (message.empty() || method_choice < 1 || method_choice > 2 || (method_choice == 2 && (key1.empty() || key2.empty()))) {
        return message;
    }

    if (method_choice == 1) {
        return shiftRightBy13(message);
    } else {
        int shift_value = getDoubleKeyShiftValue(key1, key2);
        string encrypted_message = "";

        for (char& c : message) {
            if (isalpha(c)) {
                char base = isupper(c) ? 'A' : 'a';
                c = (c - base + shift_value) % 26 + base;
            }
            encrypted_message += c;
        }

        return encrypted_message;
    }
}

int main() {
    string message;
    int method_choice;
    string key1, key2;
    
    cout << "Enter the message to encrypt: ";
    getline(cin, message);

    cout << "Enter the method choice (1 or 2): ";
    cin >> method_choice;
    cin.ignore(); // Ignore newline character

    cout << "Enter the first key: ";
    getline(cin, key1);
    cout << "Enter the second key: ";
    getline(cin, key2);
 
     
    
    string encrypted_message = message;
    if (method_choice == 1 || method_choice == 2)
       encrypted_message = getLayer1MessageEncryption(message, method_choice, key1, key2);
    cout << "The encrypted message: " << encrypted_message << endl;

    return 0;
}
