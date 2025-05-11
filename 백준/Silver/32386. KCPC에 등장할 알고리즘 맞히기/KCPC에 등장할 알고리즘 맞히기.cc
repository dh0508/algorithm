#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    map<string, int>m;
    while (t--) {
        int a, n; cin >> a >> n;
        while (n--) {
            string s; cin >> s;
            m[s] ++;
        }
    }
    string max_s;
    int max_c = -1;
    for (auto &p : m) {
        if (p.second > max_c) {
            max_c = p.second;
            max_s = p.first;
        }
        else if (p.second == max_c) {
            max_s = "-1";
        }
    }

    cout << max_s;
    return 0;
}