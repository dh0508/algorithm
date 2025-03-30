#include <bits/stdc++.h>

using namespace std;


int main() {
    int N, M; cin >> N >> M;
    vector<vector<int>>v(N, vector<int>(M,0));
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> v[i][j];
        }
    }
    int K; cin >> K;
    while (K--) {
        int i,j,x,y; cin >> i >> j >> x >> y;
        int sum = 0;
        for (int ii=i-1; ii<x; ii++) {
            for (int jj=j-1; jj<y; jj++) {
                sum += v[ii][jj];
            }
        }
        cout << sum << endl;
    }




    return 0;
}

