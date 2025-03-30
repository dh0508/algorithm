#include <bits/stdc++.h>

using namespace std;

int main() {
    long long N, M;
    cin >> N >> M;
    long long ans = 1;
    if (N>M) {
        cout << 0;
    }
    else {
        for (long long i=1; i<=N; i++) {
            ans = ans*i%M;
        }
        cout << ans;
    }


    return 0;
}