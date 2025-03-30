#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, H, W;
    cin >> N;
    cin >> H;
    cin >> W;
    string l[H];
    for (int i = 0; i < H; i++) {
        cin >> l[i];
    }
    string ans = "";
    for (int i = 0; i < N; i++) {
        ans += '?';
    }
    for (int i = 0; i < N*W; i++) {
        for (int j = 0; j < H; j++) {
            if (l[j][i] != '?') {
                ans[i/W] = l[j][i];
            }
        }
    }
    cout << ans;
    return 0;
}