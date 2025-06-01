#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; cin >> T;
    while (T--) {
        int N, M; cin >> N >> M;
        cout << (2*M - N) << " " << M - (2*M - N) << '\n';
    }
    return 0;
}