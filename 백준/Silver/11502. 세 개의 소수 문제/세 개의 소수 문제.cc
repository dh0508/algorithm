#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<bool>v(1001, true);
    v[0]=v[1]=false;
    for (int i=2; i<1001; i++) {
        if (v[i]) {
            for (int j=i+i; j<1001; j += i) {
                v[j] = false;
            }
        }
    }
    vector<int>prime_nums;
    for (int i=0; i<1001; i++) {
        if (v[i]) {
            prime_nums.push_back(i);
        }
    }

    int T; cin >> T;
    for (int i=0; i<T; i++) {
        int K; cin >> K;
        for (int i=0; i<prime_nums.size(); i++) {
            for (int j=i; j<prime_nums.size(); j++) {
                for (int k=j; k<prime_nums.size(); k++) {
                    if (prime_nums[i]+prime_nums[j]+prime_nums[k] == K) {
                        cout << prime_nums[i] << " " << prime_nums[j] << " " <<  prime_nums[k] << endl;
                        i = prime_nums.size()+1;
                        break;
                    }
                }
            }
        }
    }

    return 0;
}