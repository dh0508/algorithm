#include <bits/stdc++.h>
using namespace std;


int main() {
    int N, K, M; cin >> N >> K >> M;
    for (int i=0; i<N; i++) {
        int a; cin >> a;
    }
    while (M--) {
        int a; cin >> a;
        if (a>0) {
            if (K <= a) {
                K = abs(K-a)+1;
            }
        }
        else {
            if (K>=N+a+1) {
                K = N-abs(N+a+1-K);
            }
        }
    }
    cout << K;
    return 0;
}