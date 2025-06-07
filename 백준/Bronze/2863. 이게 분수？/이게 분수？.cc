#include <bits/stdc++.h>
using namespace std;

float cal(vector<float> v) {
    return v[0]/v[2] + v[1]/v[3];
}

int main() {
    vector<float> v(4);
    for (int i=0; i<4; i++) cin >> v[i];
    vector<float> nv = v;
    int cnt = 0;
    float val = cal(nv);
    for (int i=1; i<4; i++) {
        nv[0]=v[2]; nv[1]=v[0]; nv[2]=v[3]; nv[3]=v[1];
        v = nv;
        if (cal(nv) > val) {
            val = cal(nv);
            cnt = i;
        }
    }
    cout << cnt;
    return 0;
}