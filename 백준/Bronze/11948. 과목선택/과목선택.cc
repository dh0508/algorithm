#include <bits/stdc++.h>

using namespace std;

int main() {
	int a,b,c,d,e,f;cin>>a>>b>>c>>d>>e>>f;
	int ans=0;
	ans += max(a+b+c, max(a+b+d, max(a+c+d, b+c+d)));
	ans += max(e,f);
	cout << ans;
	return 0;
}