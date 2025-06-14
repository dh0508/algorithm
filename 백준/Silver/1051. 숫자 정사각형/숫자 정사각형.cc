#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> v(n, vector<int>(m));
    for (int i=0; i<n; i++) {
        string s; cin >> s;
        for (int j=0; j<m; j++) {
            v[i][j] = s[j] - '0';
        }
    }

    int ans = 1;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            for (int l=1; i+l<n && j+l<m; l++) {
                if (v[i][j] == v[i][j+l] &&
                    v[i][j] == v[i+l][j] &&
                    v[i][j] == v[i+l][j+l]) {
                    int size = pow((l+1),2);
                    ans = max(ans, size);
                    }
            }
        }
    }
    cout << ans;
    return 0;
}