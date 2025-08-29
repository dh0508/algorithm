#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n; cin >> n;
    if (sqrtl(n) == (long long)sqrtl(n)) {
        cout << -1;
        return 0;
    }

    long long ans = 0;

    for (long long i=1; i*i<=n; i++) {
        long long j = n - i*i;
        if (sqrtl(j) == (long long)sqrtl(j) && i <= sqrtl(j)) ans++;
    }

    for (long long i=1; i<sqrtl(n)+1; i++) {
        if (n % i == 0) {
            if (i % 2 == 0 && n / i % 2 == 0) ans ++;
            else if (i % 2 == 1 && n / i % 2 == 1) ans ++;
        }
    }


    cout << ans;

    return 0;
}