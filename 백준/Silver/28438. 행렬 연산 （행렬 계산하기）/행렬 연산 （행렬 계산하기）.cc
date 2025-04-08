#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M, Q; cin >> N >> M >> Q;
    vector<int> row(N, 0);
    vector<int> col(M, 0);

    while (Q--) {
        int how, where, what; cin >> how >> where >> what;
        if (how == 1) {
            row[where - 1] += what;
        } else {
            col[where - 1] += what;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << row[i] + col[j] << " ";
        }
        cout << '\n';
    }

    return 0;
}