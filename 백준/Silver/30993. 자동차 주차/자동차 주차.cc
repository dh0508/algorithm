#include <bits/stdc++.h>

using namespace std;

long long fac(int n) {
    long long r = 1;
    if (n<=1) {
        return 1;
    }
    else {
        while (n) {
            r *= n;
            n--;
        }
        return r;
    }
}

int main() {
    long long N, A, B, C; cin >> N >> A >> B >> C;
    cout << fac(N)/(fac(A)*fac(B)*fac(C));
    return 0;
}