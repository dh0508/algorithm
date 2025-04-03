#include <bits/stdc++.h>

using namespace std;


long long comb(int n,int r) {
    int p = 1, c = 1;
    while (r > 0) {
        c *= n--;
        p *= r--;
    }
    return c/p;
}

int main() {
    int N, M, K; cin >> N >> M >> K;

    double ans = 0.0;
    double p = comb(N, M);
    while (M >= K) {
        if (N-M >= M-K) {
            double c = comb(M, K) * comb(N-M,M-K);
            ans += c/p;
        }
        K += 1;
    }
    cout.precision(10);
    cout << ans;
    return 0;
}