#include <bits/stdc++.h>

using namespace std;


int main() {
    long long ai, bi, a, b;
    cin >> ai; cin >> bi;
    a = ai; b = bi;
    long long c;
    while (true) {
        c = max(a,b) % min(a,b);
        if (c == 0) {
            c = min(a,b);
            break;
        }
        else {
            if (a>b) {
                a = c;
            }
            else {
                b = c;
            }
        }
    }
    cout << ai*bi/c;

    return 0;
}