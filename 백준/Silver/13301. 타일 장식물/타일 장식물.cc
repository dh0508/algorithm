#include <bits/stdc++.h>

using namespace std;

int main() {
    int n; cin >> n;
    vector<long long>dp(n+1);
    dp[1]=1; dp[2]=1;
    for (int i=3; i<n+1; i++) {
        dp[i] = dp[i-1]+dp[i-2];
    }
    cout << dp[n]*4 + dp[n-1]*2;
    return 0;
}