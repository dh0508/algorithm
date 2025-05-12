#include <bits/stdc++.h>
using namespace std;

int main() {
    map<string, int>m;
    for (int i=0; i<7; i++) {
        string s; int n; cin >> s >> n;
        m[s] = n;
    }
    string maxs = "";
    int maxn = 0;
    for (auto &i : m) {
        if (maxn < i.second) {
            maxn = i.second;
            maxs = i.first;
        }
    }
    cout << maxs;
    return 0;
}