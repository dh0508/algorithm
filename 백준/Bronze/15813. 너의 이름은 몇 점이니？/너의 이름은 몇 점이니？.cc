#include <bits/stdc++.h>

using namespace std;


int main() {
    int n; cin >> n;
    string name; cin >> name;
    int ans = 0;
    for (int i=0; i<n; i++) {
        ans += name[i] - 'A' + 1;
    }
    cout << ans;
    return 0;
}