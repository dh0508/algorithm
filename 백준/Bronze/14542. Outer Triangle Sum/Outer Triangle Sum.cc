#include <bits/stdc++.h>
using namespace std;

int main() {
    int casenum=0;
    while (true) {
        int n; cin >> n;
        casenum ++;
        if (n==0) break;
        int sum=0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<i+1; j++) {
                int tmp; cin >> tmp;
                if (j==0 || j==i || i==n-1) sum += tmp;
            }
        }
        cout << "Case #"<<casenum<<":"<<sum<<'\n';
    }
    return 0;
}