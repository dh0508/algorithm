#include <bits/stdc++.h>

using namespace std;


int main() {
    int N; cin >> N;
    string s; cin >> s;
    vector<int>v;
    int cnt = 0;
    for (int i=0; i<N; i++) {
        if (s[i] == '1') {
            cnt += 1;
        }
        else {
            v.push_back(cnt);
            cnt = 0;
        }
    }
    v.push_back(cnt);
    long long ans = 0;
    for (int i=0; i<v.size(); i++) {
        long long n = (long long) v[i]*(v[i]+1)/2;
        ans += n;
    }
    cout << ans;
    return 0;
}