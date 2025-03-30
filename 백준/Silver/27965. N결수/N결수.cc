#include <bits/stdc++.h>

using namespace std;

int main() {
    long long N, K; cin >> N >> K;
    long long num=0;
    for (int i=1; i<N+1; i++) {
        num = num * long(pow(10, to_string(i).size())) % K + i % K;
    }
    cout << num%K;
    return 0;
}