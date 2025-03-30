#include <bits/stdc++.h>

using namespace std;

int main() {
    int n; cin >> n;
    vector<vector<long long>>v(n, vector<long long>(2,0));
    for (int i=0; i<n; i++) {
        cin >> v[i][1];
    }
    for (int i=0; i<n; i++) {
        cin >> v[i][0];
    }
    sort(v.begin(), v.end());
    long long ans = 0;

    for (int i=0; i<n; i++) {
        ans += (v[i][1] + v[i][0]*i);
    }
    cout << ans;

    return 0;
}