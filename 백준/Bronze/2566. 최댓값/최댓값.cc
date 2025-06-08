#include <bits/stdc++.h>
using namespace std;

int main() {
    int maxval = -1;
    int maxx, maxy;
    int a;
    for (int i=0; i<9; i++) {
        for (int j=0; j<9; j++) {
            cin >> a;
            if (a>maxval) {
                maxval = a;
                maxx = j+1;
                maxy = i+1;
            }
        }
    }
    cout << maxval<<'\n'<<maxy<<" "<<maxx;
    return 0;
}