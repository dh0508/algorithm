#include <bits/stdc++.h>

using namespace std;


int main() {
    vector<bool>prime_num(1299711, true);
    prime_num[0] = prime_num[1] = false;
    for (int i=2; i<prime_num.size(); i++) {
        if (prime_num[i]) {
            for (int j=i*2; j<prime_num.size(); j += i) {
                prime_num[j] = false;
            }
        }
    }
    vector<int>prime_num_vector;
    for (int i=1; i<prime_num.size(); i++) {
        if (prime_num[i]) {
            prime_num_vector.push_back(i);
        }
    }
    int test_case; cin >> test_case;
    for (int i=0; i<test_case;i++) {
        int N; cin >> N;
        if (find(prime_num_vector.begin(), prime_num_vector.end(), N) == prime_num_vector.end()) {
            for (int j=0; j<prime_num_vector.size(); j++) {
                if (prime_num_vector[j]>N) {
                    cout << prime_num_vector[j]-prime_num_vector[j-1] << endl;
                    break;
                }
            }
        }
        else {
            cout << 0 << endl;
        }

    }

    return 0;
}