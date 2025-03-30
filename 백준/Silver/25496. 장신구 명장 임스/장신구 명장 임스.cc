#include <bits/stdc++.h>

using namespace std;


int main() {
    int P, N; cin >> P; cin >> N;
    vector<int>v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    int cnt = 0;
    for (int i=0; i<N; i++) {
        if (P<200) {
            P += v[i]; cnt += 1;
        }
        else {
            break;
        }
    }
    cout << cnt;

    return 0;
}