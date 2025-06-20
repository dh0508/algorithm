#include <bits/stdc++.h>
using namespace std;

int main() {
    int C; cin >> C;
    while (C--) {
        string S; cin >> S;
        long long N, T, L; cin >> N >> T >> L;
        long long limit = 100000000LL * L;
        bool pass = false;

        if (S == "O(N)") pass = (N * T <= limit);
        else if (S == "O(N^2)") {
            if (N >= 31623) pass = false;
            else pass = (1LL * N * N * T <= limit);
        }
        else if (S == "O(N^3)") {
            if (N >= 1001) pass = false;
            else pass = (1LL * N * N * N * T <= limit);
        }
        else if (S == "O(2^N)") {
            if (N >= 30) pass = false;
            else {
                long long tmp = 1;
                for (int i=0; i<N; i++) {
                    tmp *= 2;
                    if (tmp > limit / T) {
                        tmp = limit + 1;
                        break;
                    }
                }
                pass = (tmp <= limit / T);
            }
        }
        else if (S == "O(N!)") {
            if (N >= 13) pass = false;
            else {
                long long tmp = 1;
                for (int i = 1; i <= N; i++) {
                    tmp *= i;
                    if (tmp > limit / T) {
                        tmp = limit + 1;
                        break;
                    }
                }
                pass = (tmp <= limit / T);
            }
        }

        if (pass) cout << "May Pass." << '\n';
        else cout << "TLE!" << '\n';
    }
    return 0;
}