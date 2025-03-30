#include <iostream>

using namespace std;

int main() {
    long p = 0;
    while (true) {
        long n;
        cin >> n;
        if (n == -1) {
            break;
        }
        p += n;
    }
    cout << p;
    return 0;
}