#include <bits/stdc++.h>

using namespace std;

int A, B;
long long ans = 0;

void solution(long long n) {
    if (n > B) {
        return;
    }
    if (n >= A && n <= B) {
        ans += 1;
    }

    solution(n*10 + 4);
    solution(n*10 + 7);
}

int main() {
    cin >> A >> B;
    solution(4); solution(7);

    cout << ans;
    
    return 0;
}