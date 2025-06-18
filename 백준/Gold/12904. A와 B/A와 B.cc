#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, t; cin >> s >> t;
    while (t.size() > s.size()) {
        if (t[t.size()-1] == 'B') {
            t.pop_back();
            reverse(t.begin(), t.end());
        }
        else {
            t.pop_back();
        }
    }
    if (t==s) cout << 1;
    else cout << 0;
    return 0;
}