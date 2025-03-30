#include <bits/stdc++.h>

using namespace std;


int main() {
    int N; cin >> N;
    map<string, int>m;
    for (int i=0; i<N; i++) {
        string a; cin >> a;
        m[a] ++;
    }

    string bestseller;
    int bestsellercnt;

    for (auto iter = m.begin(); iter != m.end(); iter++) {
        if (iter->second > bestsellercnt) {
            bestseller = iter->first;
            bestsellercnt = iter->second;
        }
    }

    cout << bestseller;

    return 0;
}