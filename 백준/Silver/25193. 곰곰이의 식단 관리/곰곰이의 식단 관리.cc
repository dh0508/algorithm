#include <bits/stdc++.h>

using namespace std;


int main() {
    int N; cin >> N;
    string S; cin >> S;
    float c_cnt = 0;
    for (int i=0; i<N; i++) {
        if (S[i] == 'C') {
            c_cnt += 1;
        }
    }
    cout << ceil(c_cnt/(N - c_cnt + 1));

    return 0;
}