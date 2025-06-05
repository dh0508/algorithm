#include <bits/stdc++.h>
using namespace std;


int main() {
    string S; cin >> S;
    int alpha[26] = {};
    for (int i = 0; i < S.length(); i++) alpha[int(S[i])-'a']++;
    for (int num : alpha) cout << num << " ";
    return 0;
}