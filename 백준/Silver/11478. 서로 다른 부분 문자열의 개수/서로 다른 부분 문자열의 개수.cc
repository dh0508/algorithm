#include <bits/stdc++.h>

using namespace std;


int main() {
    string S; cin >> S;
    set<string> set;
    string temp = "";
    for (int i=0; i < S.size(); i++) {
        for (int j=i; j < S.size(); j++) {
            temp += S[j];
            set.insert(temp);
        }
        temp = "";
    }

    cout << set.size();
}
