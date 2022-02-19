/**
 * Problem description:
 *  https://t.me/linux_bangla_programming/1003
 */
#include <cstdint>
#include <iostream>

using namespace std;

inline bool print_comma(bool not_end) {
    if (not_end) cout << ',';
    return not_end;
}

int main() {
    try {
        uint start, end;

        cout << "Start Page? ";
        cin >> start;
        cout << "End Page? ";
        cin >> end;

        if (start > end) throw "Bad input :(";

        auto pages = end - start + 1;
        auto blanks = pages % 4 == 0 ? 0 : 4 - pages % 4;
        auto papers = pages / 4 + (blanks && 1);

        if (papers > 20) throw "Too many papers needed!";

        cout << "Paper(s) Needed: " << papers << endl;
        cout << "Blank Page(s): " << blanks << endl;

        auto i = start;
        auto j = end + blanks;
        cout << "Printing order: [";
        do {
            cout << j-- << ',' << i++ << ',';
            cout << i++ << ',' << j--;
        } while (print_comma(i < j));
        cout << "]" << endl;
        return 0;
    } catch (char const* err) {
        cerr << err << endl;
        return 1;
    }
}
