#include <bits/stdc++.h>

using namespace std;

bool compare(int a, int b){
    return a > b;
}

int main() {
    int N; cin >> N;
    vector<string>v1(N);
    vector<string>v2(N);
    vector<string>v3(N);
    for (int i=0; i<N; i++) {
        string a;
        cin >> a;
        v1[i] = a;
        v2[i] = a;
        v3[i] = a;
    }
    sort(v1.begin(), v1.end());
    sort(v2.rbegin(), v2.rend());
    if (v3 == v1) {
        cout << "INCREASING";
    }
    else if (v3 == v2) {
        cout << "DECREASING";
    }
    else {
        cout << "NEITHER";
    }

    return 0;
}