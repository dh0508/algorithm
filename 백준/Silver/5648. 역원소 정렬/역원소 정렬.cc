#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

long long reverse(string s) {
    string r = " ";
    for (long long i = 0; i < s.length(); i++) {
        r = r + s[s.length()-i-1];
    }
    return stoll(r);

}
int main() {
    long long N;
    cin >> N;
    long long l[N];
    for (long long i = 0; i < N; i++) {
        cin >> l[i];
    }
    for (long long i = 0; i < N; i++) {
        l[i] = reverse(to_string(l[i]));
    }
    sort(l, l+N);
    for (long long i = 0; i<N; i++) {
        cout << l[i] << endl;
    }
    return 0;
}