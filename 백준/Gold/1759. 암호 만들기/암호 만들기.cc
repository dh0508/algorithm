#include <bits/stdc++.h>

using namespace std;

int L,C;

void dfs(vector<char>v, int n, int consonant, int vowel, string a) {
    a += v[n];

    if (v[n]=='a'||v[n]=='e'||v[n]=='i'||v[n]=='o'||v[n]=='u') {
        vowel += 1;
    }
    else {
        consonant += 1;
    }

    if (a.length() == L) {
        if (vowel>=1 && consonant >= 2) {
            cout << a << endl;
        }
        return;
    }

    for (int i=n+1; i<C; i++) {
        dfs(v,i,consonant,vowel,a);
    }
    return;
}

int main() {
    cin >> L >> C;
    vector<char>v(C);
    for (int i=0; i<C; i++) {
        cin >> v[i];
    }

    sort(v.begin(), v.end());

    for (int i=0; i<C; i++) {
        dfs(v,i,0,0,"");
    }
    return 0;
}