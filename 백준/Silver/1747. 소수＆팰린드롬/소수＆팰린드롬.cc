#include <bits/stdc++.h>

using namespace std;

bool is_palindrome(string str) {
    for (int i = 0; i < str.size() / 2; i++) {
        if (str[i] != str[str.size() - 1 - i]) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<bool> prime_num(2000001, true);
    prime_num[0] = prime_num[1] = false;
    vector<int> prime_num_vector;

    for (int i = 2; i < 2000001; i++) {
        if (prime_num[i]) {
            prime_num_vector.push_back(i);
            for (int j = i * 2; j < 2000001; j += i) {
                prime_num[j] = false;
            }
        }
    }

    int N; cin >> N;
    for (int i = 0; i < prime_num_vector.size(); i++) {
        if (N <= prime_num_vector[i]) {
            if (is_palindrome(to_string(prime_num_vector[i]))) {
                cout << prime_num_vector[i];
                break;
            }
        }
    }

    return 0;
}
