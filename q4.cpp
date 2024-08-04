#include <iostream>
#include <string>
using namespace std;

string shiftLeftBy13(string message) {
    string decrypted_message = "";

    for (char& c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            c = (c - base - 13 + 26) % 26 + base;
        }
        decrypted_message += c;
    }

    return decrypted_message;
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

string getLayer1MessageDecryption(string encrypted_message, int method_choice, string key1, string key2) {
    if (encrypted_message.empty() || method_choice < 1 || method_choice > 2 || (method_choice == 2 && (key1.empty() || key2.empty()))) {
        return encrypted_message;
    }

    if (method_choice == 1) {
        return shiftLeftBy13(encrypted_message);
    } else {
        int shift_value = getDoubleKeyShiftValue(key1, key2);
        string decrypted_message = "";

        for (char& c : encrypted_message) {
            if (isalpha(c)) {
                char base = isupper(c) ? 'A' : 'a';
                c = (c - base - shift_value + 26) % 26 + base;
            }
            decrypted_message += c;
        }

        return decrypted_message;
    }
}

int main() {
    string encrypted_message;
    string key1, key2;
    int method_choice;
    
    cout << "Enter the encrypted message: ";
    getline(cin, encrypted_message);

    cout << "Enter the method choice (1 or 2): ";
    cin >> method_choice;
    cin.ignore(); // Ignore newline character
    
    if (method_choice == 1) {
        cout << "Enter the first key: ";
        getline(cin, key1);
        cout << "Enter the second key: ";
        getline(cin, key2);
    } else if (method_choice == 2) {
        cout << "Enter the first key: ";
        getline(cin, key1);
        cout << "Enter the second key: ";
        getline(cin, key2);
    }

    string decrypted_message = getLayer1MessageDecryption(encrypted_message, method_choice, key1, key2);
    cout << "The decrypted message: " << decrypted_message << endl;

    return 0;
}
