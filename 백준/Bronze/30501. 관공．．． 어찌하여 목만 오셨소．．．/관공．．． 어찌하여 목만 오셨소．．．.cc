#include <bits/stdc++.h>

using namespace std;

int main() {
	int n; cin >> n;
	vector<string>v(n);
	for (int i=0; i<n; i++) cin >> v[i];
	for (int i=0; i<n; i++) if (v[i].find('S') != string::npos) cout << v[i];
	return 0;
}