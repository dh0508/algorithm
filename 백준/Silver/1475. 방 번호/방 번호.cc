#include <bits/stdc++.h>
using namespace std;


int main() {
    string N; cin >> N;
    vector<float>v = {0,0,0,0,0,0,0,0,0,0};
    for (int i=0; i<N.size(); i++) v[N[i]-'0'] ++;
    v[6] += v[9];
    v[9] = 0;
    v[6] /= 2;
    float max_n = 0;
    for (float i : v) {
        max_n = max(max_n, i);
    }
    cout << int(max_n+0.5);
    return 0;
}