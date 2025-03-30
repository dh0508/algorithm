#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; cin >> N;
    vector<int>v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }
    long long molecule = 1; long long denominator = v[N-1];
    long long temp;
    for (int i=N-2; i>=0; i--) {
        molecule = molecule + v[i]*denominator;
        temp = denominator;
        denominator = molecule;
        molecule = temp;
    }
    molecule = denominator - molecule;

    

    cout << molecule << " " << denominator;


    return 0;
}