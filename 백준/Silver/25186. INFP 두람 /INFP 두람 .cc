#include <bits/stdc++.h>

using namespace std;

int main() {
	int N; cin >> N;
	vector<long long> v(N);
	long long total = 0;
	
	for (int i = 0; i < N; i++) {
		cin >> v[i];
		total += v[i];
	}

	if (N == 1 && v[0] == 1) {
		cout << "Happy";
		return 0;
	}

	bool flag = true;
	for (int i = 0; i < N; i++) {
		if (total - v[i] < v[i]) {
			flag = false;
			break;
		}
	}

	cout << (flag ? "Happy" : "Unhappy");
	return 0;
}