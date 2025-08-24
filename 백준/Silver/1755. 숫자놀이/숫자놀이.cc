#include <bits/stdc++.h>
using namespace std;

vector<string>numstring = {"zero", "one", "two", "three", "four","five", "six", "seven", "eight", "nine"};

string int2string(int n) {
    string result = "";
    if (n >= 10) {
        result = numstring[n/10] + " " + numstring[n%10];
    } else {
        result = numstring[n];
    }
    return result;
}

bool cmp(pair<int, string>a, pair<int, string>b) {
    return a.second < b.second;
}

int main() {
    int N, M; cin >> N >> M;
    vector<pair<int, string>>v(M-N+1);
    for (int i=0; i<v.size(); i++) {
        v[i].first = i+N;
        v[i].second = int2string(i+N);
    }

    sort(v.begin(), v.end(), cmp);

    for (int i=0; i<v.size(); i++) {
        if (i != 0 && i % 10 == 0) cout << '\n';
        cout << v[i].first << ' ';
    }
    return 0;
}