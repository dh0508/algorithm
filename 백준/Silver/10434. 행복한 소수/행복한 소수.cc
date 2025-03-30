#include <bits/stdc++.h>

using namespace std;

vector<int>v;
bool is_happy(int M) {
    string M_s = to_string(M);
    M = 0;

    for (int i=0; i<M_s.size(); i++) {
        M += pow(M_s[i]-'0',2);
    }
    if (M == 1) {
        return true;
    }
    if (find(v.begin(), v.end(), M) == v.end()) {
        v.push_back(M);
        return is_happy(M);
    }
    else {
        return false;
    }
}

int main() {
    vector<bool>prime_num(10001, true);
    prime_num[0]=prime_num[1]=false;
    for (int i=2; i*i<=10001; i++) {
        if (prime_num[i]) {
            for (int j=i*2; j<10001; j+=i) {
                prime_num[j] = false;
            }
        }
    }
    int P; cin >> P;
    while (P--) {
        int num, M; cin >> num >> M;
        v.clear();
        if (prime_num[M] && is_happy(M)) {
            cout << num << " " << M << " " << "YES" << endl;
        }
        else {
            cout << num << " " << M << " " << "NO" << endl;
        }
    }

    return 0;
}