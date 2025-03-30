#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> v(N);
    for (int i = 0; i < N; i++) {
        cin >> v[i];
    }

    int l = 0, r = 0, value = v[0], cnt = 0;

    while (l <= r && r < N) {
        if (value < M) {
            value += v[++r];
        } else if (value == M) {
            cnt++;
            value += v[++r];
        } else {
            value -= v[l++];
            if (l > r) {
                r = l;
                if (r < N) {
                    value = v[r];
                }
            }
        }
    }

    cout << cnt;
    return 0;
}
