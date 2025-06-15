#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    string a; cin >> a;
    n--;
    int ans = 0;
    map<char, int> m;
    for (int i=0; i<a.size(); i++) m[a[i]]++;

    while (n--) {
        string b; cin >> b;
        map<char, int> bm;
        for (int i=0; i<b.size(); i++) bm[b[i]]++;

        int addcnt = 0, delcnt = 0;
        for (char ch = 'A'; ch <= 'Z'; ch++) {
            int diff = bm[ch] - m[ch];
            if (diff > 0) addcnt += diff;
            else if (diff < 0) delcnt -= diff;
        }

        if ((addcnt == 1 && delcnt == 0) ||
            (addcnt == 0 && delcnt == 1) ||
            (addcnt == 1 && delcnt == 1) ||
            (addcnt == 0 && delcnt == 0))
            ans++;
    }

    cout << ans;
    return 0;
}