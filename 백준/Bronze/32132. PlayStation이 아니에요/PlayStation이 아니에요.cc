#include <bits/stdc++.h>
using namespace std;

string solve(string s) {
    for (int i=0; i + 2<s.size(); i++) {
        string sub = s.substr(i, 3);
        if (sub == "PS4" || sub == "PS5") {
            string ans = "";
            for (int j=0; j<s.size(); j++) {
                if (j == i + 2 && isdigit(s[j])) continue;
                ans += s[j];
            }
            return solve(ans);
        }
    }
    return s;
}

int main() {
    int n; string s;
    cin >> n >> s;
    cout << solve(s) << '\n';
    return 0;
}