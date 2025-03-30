#include <bits/stdc++.h>

using namespace std;


int main() {
    int N; cin >> N;
    int L = 1, R = N;
    while (L<=R) {
        cout << L << " ";
        L += 1;
        if (L<R) {
            cout << R << " ";
            R -= 1;
        }
    }

    return 0;
}