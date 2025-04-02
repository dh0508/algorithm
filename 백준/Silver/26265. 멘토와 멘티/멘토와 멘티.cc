#include <bits/stdc++.h>

using namespace std;

bool cmp(pair<string, string>a, pair<string, string>b) {
    if (a.first == b.first) {
        return a.second > b.second;
    }
    else {
        return a.first < b.first;
    }
}

int main() {
    int N; cin >> N;
    vector<pair<string, string>>v;
    for (int i=0; i<N; i++){
        string a,b; cin >> a >> b;
        v.push_back({a,b});
    }
    sort(v.begin(), v.end(), cmp);
    for (int i=0; i<N; i++) {
        cout << v[i].first << " " << v[i].second << '\n';
    }

    return 0;
}
