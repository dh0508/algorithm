#include <bits/stdc++.h>

using namespace std;


int main() {
    int n; cin >> n;
    vector<long long>dp(n+1);
    dp[0] = 1;
    for (int i=1; i<=n; i++) {
        long long a = 0;
        for (int j=0; j<i; j++) {
            a += dp[j]*dp[i-j-1];
        }
        dp[i] = a;
    }
    cout << dp[n];
    return 0;
}