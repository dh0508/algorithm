#include <bits/stdc++.h>

using namespace std;


int main() {
    vector<bool>prime_num(100001, true);
    prime_num[0] = prime_num[1] = false;
    for (int i=2; i<=sqrt(prime_num.size()) + 1; i++) {
        if (prime_num[i]) {
            for (int j=i*i; j<prime_num.size(); j+=i) {
                prime_num[j] = false;
            }
        }
    }

    while (true) {
        string inputnum; cin >> inputnum;
        if (inputnum == "0") {
            break;
        }
        int maxnum = 0;
        for (int i=0; i<inputnum.size(); i++) {
            for (int j=1; j<=5; j++) {
                string slicenum = inputnum.substr(i, j);
                if (prime_num[stoi(slicenum)]) {
                    maxnum = max(maxnum, stoi(slicenum));
                }

            }
        }
        cout << maxnum << endl;
    }



    return 0;
}