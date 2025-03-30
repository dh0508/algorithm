#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; cin >> N;
    vector<int>v(N);
    set<int>s;
    for (int i=0; i<N; i++) {
        int a; cin >> a;
        s.insert(a);
    }
    set<int>::iterator iter;
    for (iter = s.begin(); iter != s.end(); iter++) {
        cout << *iter << " ";
    }

    return 0;
}