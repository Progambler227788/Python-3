#include <iostream>
#include <cctype>

using namespace std;


char shiftChar(char letter, int shift_value) {
    // Adjust shift_value to fit within the range of -25 to 25
    shift_value %= 26;

    // Shift the letter to the right if shift_value is positive, or to the left if negative
    if (isalpha(letter)) {
        if (isupper(letter)) {
            return ((letter - 'A' + shift_value + 26) % 26) + 'A';
        } else if (islower(letter)) {
            return ((letter - 'a' + shift_value + 26) % 26) + 'a';
        }
    }

    // Return the letter if it's not an alphabet character
    return letter;
}

int main() {
    char letter;
    int shift_value;

    cout << "Enter the letter: ";
   cin >> letter;

   cout << "Enter the shift value: ";
   cin >> shift_value;

    char shifted_letter = shiftChar(letter, shift_value);

   cout << "Letter " << letter << " was encrypted to " << shifted_letter <<endl;

    return 0;
}
