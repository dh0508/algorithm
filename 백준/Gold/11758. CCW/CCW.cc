#include <bits/stdc++.h>

using namespace std;

int main() {
    int p1x, p1y, p2x, p2y, p3x, p3y; cin >> p1x >> p1y >> p2x >> p2y >> p3x >> p3y;
    vector<int>p1p2 = {p2x-p1x, p2y-p1y};
    vector<int>p2p3 = {p3x-p2x, p3y-p2y};
    if (p1p2[0]*p2p3[1]-p1p2[1]*p2p3[0] > 0) {
        cout << 1;
    }
    else if (p1p2[0]*p2p3[1]-p1p2[1]*p2p3[0] < 0) {
        cout << -1;
    }
    else {
        cout << 0;
    }
    return 0;
}