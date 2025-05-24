#include <bits/stdc++.h>
using namespace std;


int main() {
    int x; cin >> x; x++;
    while (x<10000) {
        int a = (int)x/100;
        int b = x%100;
        if (x == pow(a+b, 2)) {
            cout << x;
            exit(0);
        }
        x ++;
    }
    cout << -1;
    return 0;
}