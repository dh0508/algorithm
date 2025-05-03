#include <bits/stdc++.h>

using namespace std;

int main() {
    int n; cin >> n;
    vector<vector<int>>v(n, vector<int>(2));
    for (int i=0; i<n; i++) {
        int a, b; cin >> a >> b;
        v[i][0] = a; v[i][1] = b;
    }
    sort(v.begin(), v.end());
    int ans = 0, price = 0;
    for (int i=0; i<n; i++) {
        int tmpprice = 0;
        for (int j=0; j<n; j++) {
            if (v[i][0] <= v[j][0] && v[i][0] > v[j][1]) {
                tmpprice += v[i][0]-v[j][1];
            }
        }
        if (tmpprice > price) {
            price = tmpprice;
            ans = v[i][0];
        }
    }
    cout << ans;
    return 0;
}