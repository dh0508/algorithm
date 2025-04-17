#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, m; cin >> n >> m;
	vector<int>v(n);
	for(int i=0; i<n; i++){
		cin >> v[i];
	}

	long long ans = 0;
	long long tmp = 0;
	for(int i=0; i<m; i++){
		tmp += v[i];
	}
	ans = tmp;
	for (int i=0; i<n-m; i++){
		tmp -= v[i];
		tmp += v[m+i];
		ans = max(ans, tmp);
	}
	cout << ans;
	return 0;
}