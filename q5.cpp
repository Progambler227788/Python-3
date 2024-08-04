#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string getLayer2MessageEncryption(string message, string key_phrase) {
    if (message.empty() || key_phrase.empty()) {
        return message;
    }

    // Construct the key from the key phrase
    string key;
    for (size_t i = 0; i < key_phrase.length(); ++i) {
        if (isalpha(key_phrase[i])) {
            key += toupper(key_phrase[i]);
            while (i + 1 < key_phrase.length() && isalpha(key_phrase[i + 1])) {
                ++i; // Skip to the next word
            }
        }
    }

    if (key.empty()) {
        return message;
    }

    // Calculate the shift values for each character of the key
    string shift_values;
    for (char c : key) {
        int shift_value = c - 'A';
        shift_values += to_string(shift_value) + " ";
    }

    // Encrypt the message using the shift values calculated from the key
    string encrypted_message = "";
    int shift_index = 0;
    for (char c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            int shift_value = key[shift_index % key.length()] - 'A';
            c = (c - base + shift_value) % 26 + base;
            shift_index++;
        }
        encrypted_message += c;
    }

    return encrypted_message;
}

int main() {
    string message, key_phrase;
    cout << "Enter the message to encrypt: ";
    getline(cin, message);
    cout << "Enter the key phrase: ";
    getline(cin, key_phrase);
    string encrypted_message = getLayer2MessageEncryption(message, key_phrase);
    cout << "The encrypted message: " << encrypted_message << endl;
    return 0;
}
