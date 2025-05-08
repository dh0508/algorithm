#include <bits/stdc++.h>
using namespace std;


int main() {
    map<string, int>m;
    int n; cin >> n;
    for (int i=0; i<n; i++) {
        string fruit; int fruit_n; cin >> fruit >> fruit_n;
        m[fruit] += fruit_n;
    }
    if (m["STRAWBERRY"]==5||m["BANANA"]==5||m["LIME"]==5||m["PLUM"]==5)cout << "YES";
    else cout << "NO";
    return 0;
}