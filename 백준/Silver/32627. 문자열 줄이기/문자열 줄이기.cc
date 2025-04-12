#include <bits/stdc++.h>

using namespace std;


int main() {
    int N, M; cin >> N >> M;
    string s; cin >> s;
    string ss = s;
    sort(ss.begin(), ss.end());
    int cnt = 0;
    while (M--) {
        s.erase(s.find(ss[cnt]),1);
        cnt ++;
    }
    cout << s;
    return 0;
}