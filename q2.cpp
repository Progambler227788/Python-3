#include <iostream>
#include <string>

using namespace std;

int getDoubleKeyShiftValue(string key1, string key2) {
    int count = 0;
    
    // Iterate over each character in key1
    for (char c1 : key1) {
        // Iterate over each character in key2
        for (char c2 : key2) {
            // If characters match, increment count
            if (c1 == c2) {
                count++;
                break; // Break the inner loop if a match is found
            }
        }
    }
    
    return count;
}

int main() {
    string key1, key2;
    
    cout << "Enter the first key: ";
    getline(cin, key1);
    
    cout << "Enter the second key: ";
    getline(cin, key2);
    
    int shift_distance = getDoubleKeyShiftValue(key1, key2);
    cout << "The shift distance: " << shift_distance << endl;
    
    return 0;
}
