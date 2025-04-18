#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;
    int cnt = 0;

    while (N != 0) {
        cnt++;
        string strN = to_string(N);
        int pos = strN.find('1');

        if (pos != string::npos) {
            strN.erase(pos, 1);
            if (strN.empty()) {
                N = 0;
            } else {
                N = stoll(strN);
            }
        }
        else {
            N -= 1;
        }
    }

    cout << cnt;
    return 0;
}