#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9;

int main() {
    int n; cin >> n;

    int offset = abs(n);
    vector<long long> dp(2 * offset + 1);
    dp[offset] = 0;
    if (offset >= 1) {
        dp[offset + 1] = 1;
        dp[offset - 1] = 1;
    }

    for (int i = offset + 2; i <= 2 * offset; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }

    for (int i = offset - 2; i >= 0; i--) {
        dp[i] = (-dp[i + 1] + dp[i + 2]) % MOD;
    }

    long long result = dp[n + offset];
    if (result > 0) {
        cout << 1 << '\n' << result;
    } else if (result < 0) {
        cout << -1 << '\n' << -result;
    } else {
        cout << 0 << '\n' << 0;
    }

    return 0;
}