#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    while (n--) {
        string a; cin >> a;
        int cnt = 0;

        if (a.size() >= 3) {
            for (int i = 0; i <= a.size() - 3; i++) {
                if (a[i] == 'W' && a[i+1] == 'O' && a[i+2] == 'W') {
                    cnt++;
                }
            }
        }
        cout << cnt << '\n';
    }
    return 0;
}