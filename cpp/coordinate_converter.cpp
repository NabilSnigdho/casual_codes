/**
 * Problem description:
 *  https://t.me/linux_bangla_programming/60
 */
#include <iostream>

using namespace std;
struct Point {
    int x, y;
};

int main() {
    Point p;
    int current_coord, target_coord;
    cout << "Enter x, y, current_coordinate, target_coordinate" << endl;
    cin >> p.x >> p.y >> current_coord >> target_coord;
    switch ((current_coord - 1) ^ (target_coord - 1)) {
        case 0:
            break;
        case 1:
            p = Point{-p.x, +p.y};
            break;
        case 2:
            p = Point{-p.x, -p.y};
            break;
        case 3:
            p = Point{+p.x, -p.y};
            break;
        default:
            cerr << "Invalid Input" << endl;
            return 1;
    }
    cout << "New value of x and y in the target coordinate is (" << p.x << ", "
         << p.y << ")." << endl;
    return 0;
}