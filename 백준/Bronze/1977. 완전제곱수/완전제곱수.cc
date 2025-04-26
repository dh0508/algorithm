#include <bits/stdc++.h>

using namespace std;


int main() {
    int N, M; cin >> N >> M;
    vector<int>v;
    for (int i=N; i<M+1; i++) {
        if (sqrt(i) == int(sqrt(i))) {
            v.push_back(i);
        }
    }
    long long sum = 0;
    int min = INT_MAX;
    if (v.size() == 0) {
        cout << -1;
    }
    else {
        for (int i=0; i<v.size(); i++) {
            sum += v[i];
            if (min > v[i]) {
                min = v[i];
            }
        }
        cout << sum << '\n' << min;
        return 0;
    }
}