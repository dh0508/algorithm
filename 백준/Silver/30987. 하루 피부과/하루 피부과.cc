#include <bits/stdc++.h>
using namespace std;

int myintegral(int x, int a, int b, int c, int d, int e);

int main() {
    int x1, x2; cin >> x1 >> x2;
    int a, b, c, d, e; cin >> a >> b >> c >> d >> e;
    cout << (myintegral(x2, a, b, c, d, e) - myintegral(x1, a, b, c, d, e));
    return 0;
}

int myintegral(int x, int a, int b, int c, int d, int e) {
    return a * (x * x * x) / 3 + (b - d) * (x * x) / 2 + (c - e) * x;
}