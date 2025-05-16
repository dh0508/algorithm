#include <bits/stdc++.h>

using namespace std;

int main() {
	int t; cin >> t;
	for (int i=1; i<=t; i++) {
		int n; cin >> n;
		vector<int>v(n);
		for (int j=0; j<n; j++) cin >> v[j];
		sort(v.begin(), v.end());
		int gap = 0; int forcmp = v[0];
		for (int j=1; j<n; j++) {
			gap = max(gap, v[j]-forcmp);
			forcmp = v[j];
		}
		cout << "Class "<<i<<'\n';
		cout << "Max "<<v[n-1]<<", Min "<<v[0]<<", Largest gap "<<gap<<'\n';
	}
	return 0;
}