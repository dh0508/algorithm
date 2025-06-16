#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, K; cin >> N >> M >> K;
    vector<int> v(N);
    for (int i=0; i<N; i++) cin >> v[i];
    unordered_map<int, int> freq;
    long long ans = 0;

    for (int i=0; i<N; i++) {
        ans += freq[v[i] ^ K];
        freq[v[i]]++;
        if (i >= M) {
            freq[v[i - M]]--;
            if (freq[v[i - M]] == 0) freq.erase(v[i - M]);
        }
    }
    cout << ans;
    return 0;
}