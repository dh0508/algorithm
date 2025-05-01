#include <bits/stdc++.h>

using namespace std;

bool is_prime(long long n) {
    if (n < 2) {
        return false;
    }
    for (long long i = 2; i * i <= n; ++i)
        if (n % i == 0) {
            return false;
        }
    return true;
}

int main() {
    int t; cin >> t;
    while (t--) {
        long long n; cin >> n;
        while (true) {
            if (is_prime(n)) {
                cout << n << '\n';
                break;
            }
            n++;
        }
    }
    return 0;
}