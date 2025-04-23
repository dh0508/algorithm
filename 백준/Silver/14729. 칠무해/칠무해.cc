#include<bits/stdc++.h>
using namespace std;

int main(){
	int N; cin >> N;
	vector<float>v;
	while(N--){
		float a; cin >> a;
		v.push_back(a);
	}
	sort(v.begin(), v.end());
    cout << fixed << setprecision(3);
	for(int i=0; i<7; i++){
		cout << v[i] << '\n';
	}
	return 0;
}