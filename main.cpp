#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

struct wordRecord 
{
    string word;
    int count;
};

void getIgnoreWords(const char *ignoreWordFileName, string ignoreWords[]);
bool isIgnoreWord(string word, string ignoreWords[]);
int getTotalNumberNonIgnoreWords(wordRecord distinctWords[], int length);
void sortArray(wordRecord distinctWords[], int length);
void printTenFromN(wordRecord distinctWords[], int N, int totalNumWords);

int main(int argc, char*argv[]) {
    if (argc != 4) {
        cout << "Usage: Assignment2Solution <number of words> <inputfilename.txt> <ignoreWordsfilename.txt>" <<endl;
        return 1;
    }
    int capacity = 100;
    int size = 0;
    int doubles = 0; 
    string ignoreWords[50];
    wordRecord *unique = new wordRecord[capacity];

    getIgnoreWords(argv[3], ignoreWords);
    ifstream inStream;
    inStream.open(argv[2]);
    string word;
    bool flag;
    while (inStream >> word) {
        flag = 0;
        if (!isIgnoreWord(word, ignoreWords)) {
            for (int i = 0; i < size; i++) {
                if (word == unique[i].word) {
                    unique[i].count += 1;
                    flag = 1;
                    break;
                }
            }
            if ((size >= capacity) && !flag) {
                wordRecord* temp = new wordRecord[capacity*2];
                for (int i = 0; i < capacity; i++) {
                    temp[i] = unique[i];
                }
                delete[] unique;
                unique = temp;
                capacity = capacity*2;
                doubles += 1;
            }
            if (!flag) {
                unique[size].word = word;
                unique[size].count = 1;
                size += 1;
            }
        }
    }
    cout << "Array doubled: " << doubles << endl;
    cout << "Distinct non-common words: " << size << endl;
    int totalNonIgnores = getTotalNumberNonIgnoreWords(unique, size);
    cout << "Total non-common words: " << totalNonIgnores << endl;
    cout << "Probability of next 10 words from rank " << argv[1] << endl;
    cout << "---------------------------------------" << endl;
    sortArray(unique, size);
    printTenFromN(unique, stoi(argv[1]), totalNonIgnores);
}

void getIgnoreWords(const char *ignoreWordFileName, string ignoreWords[]) {
    ifstream inStream;
    int i = 0;
    inStream.open(ignoreWordFileName);
    string word;
    while (inStream >> word ){
        ignoreWords[i] = word;
        i++;
    }
    inStream.close();
}

bool isIgnoreWord(string word, string ignoreWords[]) {
    for (int i = 0; i < 50; i++) {
        if (word == ignoreWords[i]) {
            return 1;
        }
    }
    return 0;
}

int getTotalNumberNonIgnoreWords(wordRecord distinctWords[], int length) {
    int total = 0;
    for (int i = 0; i < length; i++) {
        total += distinctWords[i].count;
    }
    return total;
}

void sortArray(wordRecord distinctWords[], int length) {
    wordRecord tempVal;
    for (int i = 0; i < length - 1;i++) {
        for (int j = 0; j < length - i - 1; j++) {
            if (distinctWords[j].count < distinctWords[j+1].count) {
                tempVal = distinctWords[j];
                distinctWords[j] = distinctWords[j+1];
                distinctWords[j+1] = tempVal;
            }
            if (distinctWords[j].count == distinctWords[j+1].count) {
                if (distinctWords[j].word > distinctWords[j+1].word) {
                    tempVal = distinctWords[j];
                    distinctWords[j] = distinctWords[j+1];
                    distinctWords[j+1] = tempVal;
                }
            }
        }
    }
}

void printTenFromN(wordRecord distinctWords[], int N, int totalNumWords) {
    cout << fixed;
    cout << setprecision(5);
    for (int i = N; i < (9+N); i++) {
        cout << (float) distinctWords[i].count/totalNumWords << " - " << distinctWords[i].word << endl;
    }
    cout << (float) distinctWords[N+9].count/totalNumWords << " - " << distinctWords[N+9].word;
}
