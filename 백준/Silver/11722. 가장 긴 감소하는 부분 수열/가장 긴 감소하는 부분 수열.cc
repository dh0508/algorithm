#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; cin >> N;
    vector<int>v(N);
    vector<int>dp(N,1);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<i; j++) {
            if (v[j] > v[i]) {
                dp[i] = max(dp[i], dp[j]+1);
            }
        }
    }
    int max_value = 0;
    for (int i=0; i<N; i++) {
        max_value = max(max_value, dp[i]);
    }
    cout << max_value;

    return 0;
}