#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; cin >> N;
    cin.ignore();
    for (int i=1; i<=N; i++) {
        string a; getline(cin, a);
        cout << i<<". "<<a<<endl;
    }
    return 0;
}