#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<bool> prime(50001, true);
    vector<int> prime_num;
    prime[0] = prime[1] = false;
    for (int i = 2; i < 50001; i++) {
        if (prime[i]) {
            prime_num.push_back(i);
            for (int j = i + i; j < 50001; j += i) {
                prime[j] = false;
            }
        }
    }

    vector<long long> prime_multiple;
    int prime_size = prime_num.size();

    for (int i = 0; i < prime_size; i++) {
        for (int j = i + 1; j < prime_size; j++) {
            long long product = (long long)prime_num[i] * prime_num[j];
            if (product <= 1000000) {
                prime_multiple.push_back(product);
            }
        }
    }

    sort(prime_multiple.begin(), prime_multiple.end());

    int T; cin >> T;
    while (T--) {
        int K; cin >> K;
        int left = 0, right = prime_multiple.size() - 1;
        int result = -1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (prime_multiple[mid] >= K) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        cout << prime_multiple[result] << endl;
    }

    return 0;
}
