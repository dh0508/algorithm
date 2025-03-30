#include <bits/stdc++.h>

using namespace std;

bool can_win(int n) {
    int winnum;
    if (30 % (n+1) == 0) {
        winnum = n+1;
    }
    else {
        winnum = 30 % (n+1);
    }
    if (winnum > n) {
        return true;
    }
    else {
        return false;
    }
}
int main() {
    int A; cin >> A;
    for (int i=1; i < A+1; i++) {
        if (can_win(i)) {
            cout << i << endl;
        }
    }
    return 0;
}