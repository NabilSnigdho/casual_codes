#include <iostream>

using namespace std;

int main() {
    string word;
    cin >> word;
    auto left = word.cbegin(), right = --word.cend();
    bool is_palindrome = true;
    do {
        if (*left != *right) {
            is_palindrome = false;
            break;
        }
    } while (++left < --right);
    cout << word << (is_palindrome ? " is" : " isn't")
         << " a palindrome" << endl;
    return 0;
}
