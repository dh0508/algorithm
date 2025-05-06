#include <bits/stdc++.h>
using namespace std;

bool cmp (const string& a, const string& b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a <= b;
}

string add (const string& x, const string& y) {
    string res;
    int carry = 0;
    int i = x.size() - 1, j = y.size() - 1;
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += x[i--] - '0';
        if (j >= 0) sum += y[j--] - '0';
        res += sum % 10 + '0';
        carry = sum / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    while (true) {
        string a, b; cin >> a >> b;
        if (a == "0" && b == "0") break;
        string x = "1", y = "2";
        int cnt = 0;
        while (cmp(x, b)) {
            if (cmp(a, x)) cnt++;
            string tmp = x;
            x = y;
            y = add(tmp, y);
        }

        cout << cnt << '\n';
    }
    return 0;
}