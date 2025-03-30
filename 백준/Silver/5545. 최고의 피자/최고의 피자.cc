#include <bits/stdc++.h>

using namespace std;


int main() {
    int N; cin >> N;
    int A, B; cin >> A; cin >> B;
    int C; cin >> C;
    vector<int>v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }
    sort(v.rbegin(),v.rend());
    int price = A, calorie = C;
    for (int i=0; i<N; i++) {
        if (calorie/float(price) < float(v[i])/B) {
            price += B; calorie += v[i];
        }
    }
    cout << calorie/price;
    return 0;
}