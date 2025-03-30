#include <bits/stdc++.h>

using namespace std;


int main() {
    int N; cin >> N;
    vector<int>v(N);
    for (int i=0; i<N ;i++) {
        cin >> v[i];
    }
    int high_num = N;
    int correct_cnt = 0;
    for (int i=N-1; i>-1; i--) {
        if (v[i] == high_num) {
            correct_cnt += 1;
            high_num -= 1;
        }
    }
    cout << N-correct_cnt;
    
    return 0;
}