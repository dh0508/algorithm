#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; cin >> N;
    vector<int>v(N);
    for (int i=0;i<N;i++) {
        cin >> v[i];
    }
    sort(v.rbegin(),v.rend());
    int ans = 0;
    for (int i=0;i<N;i++) {
        if ((i+1)%3 == 0) {
            continue;
        }
        else {
            ans += v[i];
        }
    }
    cout << ans;
    return 0;
}