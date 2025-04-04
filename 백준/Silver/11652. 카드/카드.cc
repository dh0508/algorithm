#include <bits/stdc++.h>

using namespace std;

bool cmp(pair<long long, int>a, pair<long long, int>b) {
    if (a.second == b.second) {
        return a.first < b.first;
    }
    return a.second > b.second;
}

int main() {
    int N; cin >> N;
    map<long long, int>m;
    while (N--) {
        long long a; cin >> a;
        m[a] ++;
    }
    vector<pair<long long, int>>v(m.begin(), m.end());
    sort(v.begin(), v.end(), cmp);
    cout <<  v[0].first;
    return 0;
}