#include <bits/stdc++.h>

using namespace std;


int main() {
    vector<bool>prime_num(40001, true);
    prime_num[0]=prime_num[1] = false;
    for (int i=2; i<prime_num.size(); i++) {
        if (prime_num[i]) {
            for (int j=i*i; j<prime_num.size(); j+=i) {
                prime_num[j] = false;
            }
        }
    }
    int N; cin >> N;
    vector<int>dp(40001,0);
    dp[0] = 1;
    for (int i=2; i<dp.size(); i++) {
        if (prime_num[i]) {
            for (int j=i; j<dp.size(); j++) {
                dp[j] += dp[j-i];
                dp[j] %= 123456789;
            }
        }
    }
    cout << dp[N]%123456789;
    return 0;
}