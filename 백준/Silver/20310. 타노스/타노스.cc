#include <bits/stdc++.h>

using namespace std;

int main() {
    string s; cin >> s;
    int zero_cnt = 0; int one_cnt = 0;
    for (int i=0; i<s.size(); i++) {
        if (s[i] == '1') {
            one_cnt += 1;
        }
        else if (s[i] == '0') {
            zero_cnt += 1;
        }
    }
    int cnt = 0;
    for (int i=0; i<s.size(); i++) {
        if (cnt == one_cnt/2) {
            break;
        }
        if (s[i] == '1') {
            s.erase(i,1); s.insert(i,"2");
            cnt += 1;
        }
    }
    cnt = 0;
    for (int i=s.size(); i>0; i--) {
        if (cnt == zero_cnt/2) {
            break;
        }
        if (s[i] == '0') {
            s.erase(i,1);
            cnt += 1;
        }
    }

    for (int i=0; i<s.size(); i++) {
        if (s[i] == '2') {
            continue;
        }
        else {
            cout << s[i];
        }
    }
    return 0;
}