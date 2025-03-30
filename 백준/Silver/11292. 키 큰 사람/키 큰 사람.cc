#include <bits/stdc++.h>

using namespace std;

bool cmp(pair<string, float>&a, pair<string, float>&b) {
    return a.second > b.second;
}

int main() {
    while (true) {
        int N; cin >> N;
        if (N == 0) {
            return 0;
        }
        vector<pair<string, float>> v;
        string name; float height;
        for (int i=0; i<N; i++) {
            cin >> name >> height;
            v.push_back({name, height});
        }

        sort(v.begin(), v.end(), cmp);

        for (int i=0; i<N; i++) {
            if (v[i].second == v[0].second) {
                cout << v[i].first << " ";
            }
        }
        cout << endl;
    }
    
    return 0;
}