#include <bits/stdc++.h>

using namespace std;


void sol(int num, int N, const vector<int>& v, int& ans);

bool cmp(int a, int b) {
    return a>b;
}

int main() {
    int N, K; cin >> N >> K;
    vector<int> v(K);
    for (int i = 0; i < K; i++) {
        cin >> v[i];
    }
    sort(v.begin(), v.end(), cmp);
    int ans = 0;
    sol(0, N, v, ans);
    cout << ans << endl;

    return 0;
}


void sol(int num, int N, const vector<int>& v, int& ans) {
    if (num > N) {
        return;
    }
    ans = max(ans, num);
    for (int i=0; i<v.size(); i++) {
        sol(num * 10 + v[i], N, v, ans);
    }
}