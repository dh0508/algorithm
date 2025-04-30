#include <bits/stdc++.h>

using namespace std;

bool is_lucky(string s) {
    if (s.size() % 2 != 0) return false;
    int l=0, r=0;
    for (int i=0; i<s.size()/2; i++) {
        l += s[i]-'0';
    }
    for (int i=s.size()/2; i<s.size(); i++) {
        r += s[i]-'0';
    }
    return l==r;
}

int main() {
    string s; cin >> s;
    for (int len = s.size(); len >= 2; len--) {
        for (int i=0; i+len <= s.size(); i++) {
            string ss = s.substr(i, len);
            if (is_lucky(ss)) {
                cout << len;
                return 0;
            }
        }
    }
    cout << 0;
    return 0;
}