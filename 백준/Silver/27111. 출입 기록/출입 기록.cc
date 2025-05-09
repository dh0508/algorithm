#include <bits/stdc++.h>
using namespace std;


int main() {
    int N; cin >> N;
    vector<bool>is_in(200001, false);
    int ans = 0;
    for (int i=0; i<N; i++) {
        int a, b; cin >> a >> b;
        if (b) {
            if (is_in[a]) ans += 1;
            is_in[a] = true;
        }
        else {
            if (!is_in[a]) ans += 1;
            is_in[a] = false;
        }
    }
    for (int i=1; i<200001; i++) {
        if (is_in[i]) ans += 1;
    }
    cout << ans;
    return 0;
}