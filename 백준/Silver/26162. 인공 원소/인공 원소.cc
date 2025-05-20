#include <bits/stdc++.h>
using namespace std;


bool isPrime(int n) {
    if (n < 2) return false;
    for (int i=2; i*i<=n; i++)
        if (n % i == 0) return false;
    return true;
}

int main() {
    int N; cin >> N;
    vector<int> atoms(N);
    for (int i=0; i<N; i++) {
        cin >> atoms[i];
    }
    
    vector<int> primes;
    for (int i=2; i<119; i++) {
        if (isPrime(i)) primes.push_back(i);
    }

    for (int a : atoms) {
        bool found = false;
        for (int i=0; i<primes.size(); i++) {
            for (int j=i; j<primes.size(); j++) {
                if (primes[i] + primes[j] == a) {
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        cout << (found ? "Yes" : "No") << '\n';
    }

    return 0;
}