# include <bits/stdc++.h>

using namespace std;


int main() {
    string jinho; cin >> jinho;
    int n; cin >> n;
    int cnt = 0;
    for (int i=0; i<n; i++) {
        string tmp; cin >> tmp;
        if (tmp == jinho) cnt += 1;
    }
    cout << cnt;
    return 0;
}