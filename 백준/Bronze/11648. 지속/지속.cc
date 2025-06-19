#include <bits/stdc++.h>
using namespace std;

int main() {
    string s; cin >> s;
    int cnt = 0;
    while (s.size() > 1) {
        int n = 1;
        for (char c : s) {
            n *= (c - '0');
        }
        s = to_string(n);
        cnt++;
    }
    cout << cnt;
    return 0;
}