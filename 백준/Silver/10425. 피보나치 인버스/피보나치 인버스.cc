#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    long long A = 1, B = 1, temp;
    map<long long, int> mp;

    for (int i = 2; i < 100001; i++) {
        temp = A + B;
        A = B;
        B = temp;
        if (B > 99999999999999999LL) {
            B -= 100000000000000000LL;
        }
        mp[A] = i;
    }

    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        long long val = 0;
        for (size_t j = 0; j < s.size(); j++) {
            val = val * 10 + (s[j] - '0');
            val %= 100000000000000000LL;
        }
        cout << mp[val] << endl;
    }

    return 0;
}