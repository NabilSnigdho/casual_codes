#include <iostream>
#include <cstdint>

using namespace std;

int main() {
    uint a;
    cin >> oct >> a;
    const uint base = 2;

    string binary = "";
    while (a > 0) {
        binary += '0' + (a % base);
        a /= base;
    }

    // print buffer in reverse order
    for (int i = binary.length() - 1; i >= 0; --i)
        cout << binary[i];
    cout << endl;

    return 0;
}