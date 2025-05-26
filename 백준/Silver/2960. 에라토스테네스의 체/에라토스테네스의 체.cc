#include <bits/stdc++.h>
using namespace std;


int main() {
    int N, K; cin >> N >> K;
    vector<bool>v(N+1, true);
    v[1]= false;
    int cnt = 0;
    for (int i=2; i<v.size(); i++) {
        if (v[i]) {
            cnt++;
            if (cnt == K) {
                cout << i;
                break;
            }
            for (int j=i+i; j<v.size(); j += i) {
                if (v[j]) {
                    v[j] = false;
                    cnt ++;
                    if (cnt == K) {
                        cout << j;
                        break;
                    }
                }
            }
        }
    }
    return 0;
}