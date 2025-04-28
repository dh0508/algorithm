#include <bits/stdc++.h>

using namespace std;


int main() {
    int N; cin >> N;
    int ans = 0;
    vector<int>v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }
    vector<int>vv(4);
    for (int i=0; i<N-3; i++) {
        for (int j=i+1; j<N-2; j++) {
            for (int k=j+1; k<N-1; k++) {
                int tmp = 1;
                for (int l=0; l<=i; l++) {
                    tmp *= v[l];
                }
                vv[0] = tmp;
                tmp = 1;
                for (int l=i+1; l<=j; l++) {
                    tmp *= v[l];
                }
                vv[1] = tmp;
                tmp = 1;
                for (int l=j+1; l<=k; l++) {
                    tmp *= v[l];
                }
                vv[2] = tmp;
                tmp = 1;
                for (int l=k+1; l<N; l++) {
                    tmp *= v[l];
                }
                vv[3] = tmp;
                ans = max(ans, vv[0]+vv[1]+vv[2]+vv[3]);
            }
        }
    }
    cout << ans;
    return 0;
}