#include <bits/stdc++.h>

using namespace std;

bool is_in(string p, string s, int n) {
    for (int i=0; i<s.size(); i++) {
        if (p[n+i] != s[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    int T; cin >>T;
    while (T--) {
        string s, p; cin >> s >> p;
        int sec = 0;
        for (int i=0; i<s.size(); i++) {
            if (s[i] == p[0]) {
                if (is_in(s, p, i)) {
                    sec += 1;
                    i += (p.size() - 1);
                }
            }
        }
    cout << s.size() - p.size()*sec + sec << '\n';
    }
    return 0;
}