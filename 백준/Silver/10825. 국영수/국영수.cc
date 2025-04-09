#include <bits/stdc++.h>

using namespace std;

bool cmp(const pair<string, vector<int>>&a, const pair<string, vector<int>>&b) {
    if (a.second[0] == b.second[0]) {
        if (a.second[1] == b.second[1]) {
            if (a.second[2] == b.second[2]) {
                return a.first < b.first;
            }
            return a.second[2] > b.second[2];
        }
        return a.second[1] < b.second[1];
    }
    return a.second[0] > b.second[0];
}

int main() {
    int t; cin >> t;
    vector<pair<string, vector<int>>> v;

    for (int i=0; i<t; i++) {
        string name; int a, b, c;
        cin >> name >> a >> b >> c;
        v.push_back(pair<string, vector<int>>(name, {a, b, c}));
    }
    sort(v.begin(), v.end(), cmp);

    for (int i=0; i<t; i++) {
        cout << v[i].first << '\n';
    }
    return 0;
}