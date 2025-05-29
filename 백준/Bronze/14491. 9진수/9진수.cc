#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    string ans = "";
    ans += to_string(t / (int)pow(9,4));
    t %= (int)pow(9,4);
    ans += to_string(t / (int)pow(9,3));
    t %= (int)pow(9,3);
    ans += to_string(t / (int)pow(9,2));
    t %= (int)pow(9,2);
    ans += to_string(t / 9);
    t %= 9;
    ans += to_string(t);
    cout << stoi(ans);
    return 0;
}