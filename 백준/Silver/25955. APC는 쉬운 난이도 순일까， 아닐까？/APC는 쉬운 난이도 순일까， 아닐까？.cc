#include <bits/stdc++.h>

using namespace std;

string difficulty = "BSGPD";
bool cmp(string a, string b) {
	if (difficulty.find(a[0]) == difficulty.find(b[0])) {
		return stoi(a.substr(1)) > stoi(b.substr(1));
	}
	return difficulty.find(a[0]) < difficulty.find(b[0]);
}

int main() {
	int n; cin >> n;
	vector<string>v(n);
;	for (int i=0; i<n; i++) cin >> v[i];
	vector<string>vv=v;
	sort(v.begin(), v.end(), cmp);
	if (vv==v) cout << "OK";
	else {
		cout << "KO\n";
		for (int i=0; i<n; i++) {
			if (v[i]!=vv[i]) cout << v[i] << ' ';
		}
	}
	return 0;
}