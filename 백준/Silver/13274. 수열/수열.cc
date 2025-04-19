#include <bits/stdc++.h>

using namespace std;

int main(){
    int N, K; cin >> N >> K;
    vector<long long>v(N);
    for(int i=0; i<N; i++){
        cin >> v[i];
    }
    while(K--){
        int L, R, X; cin >> L >> R >> X;
        sort(v.begin(), v.end());
        for(int i=L-1; i<R; i++){
            v[i] += X;
        }
    }
    sort(v.begin(), v.end());
    for (int i=0; i<N; i++){
        cout << v[i] << ' ';
    }
	
    return 0;
}