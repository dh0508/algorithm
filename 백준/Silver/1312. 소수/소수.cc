#include <bits/stdc++.h>

using namespace std;

int main() {
    int A, B, N;
    cin >> A >> B >> N;

    int result = 0;
    for (int i = 0; i < N; i++) {
        A = (A % B) * 10;
        result = A / B;
    }

    cout << result;
    return 0;
}
