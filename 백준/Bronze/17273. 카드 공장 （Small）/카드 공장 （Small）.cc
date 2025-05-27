#include <bits/stdc++.h>
using namespace std;


int main() {
    int N, M; cin >> N >> M;
    vector<int>vf(N);
    vector<int>vb(N);
    for (int i=0;  i<N; i++) cin >> vf[i] >> vb[i];
    vector<int>v = vf;
    for (int i=0; i<M; i++) {
        int K; cin >> K;
        for (int j=0; j<N; j++) {
            if (v[j]<=K) {
                if (v[j] == vf[j]) v[j] = vb[j];
                else v[j] = vf[j];
            }
        }
    }
    int ans = 0;
    for (int i=0; i<N; i++) ans += v[i];
    cout << ans;

    return 0;
}