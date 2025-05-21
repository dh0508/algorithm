#include <bits/stdc++.h>
using namespace std;


int main() {
    int t; cin >> t;
    while (t--) {
        int a, b; cin >> a >> b;
        long long ans = 1;
        for (int i=0; i<b; i++) {
            ans = ans * a % 10;
        }
        if (ans == 0) cout << 10 << '\n';
        else cout << ans << '\n';
    }
    return 0;
}