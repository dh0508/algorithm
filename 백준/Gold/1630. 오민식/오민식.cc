#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; cin >> N;
    long long ans = 1;
    vector<int> prime_num(N + 1, 0);

    for (int i = 2; i <= N; i++) {
        if (prime_num[i] == 0) {
            int cnt = 1;
            for (int j = i * 2; j <= N; j += i) {
                prime_num[j] = 1;
                int t = j, temp = 0;
                while (t % i == 0 && t > 1) {
                    t /= i;
                    temp++;
                }
                cnt = max(cnt, temp);
            }
            for (int j = 0; j < cnt; j++) {
                ans = (ans * i) % 987654321;
            }
        }
    }

    cout << ans;
    return 0;
}