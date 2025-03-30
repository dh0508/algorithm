#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; cin >> N;
    while (N--) {
        int G; cin >> G;
        vector<int> v(G);
        for (int i=0; i<G; i++) {
            cin >> v[i];
        }

        int cnt = 1;
        while (true) {
            unordered_set<int> s;
            for (int i=0; i<G; i++) {
                s.insert(v[i] % cnt);
            }

            if (s.size() == G) {
                cout << cnt << endl;
                break;
            }
            cnt += 1;
        }
    }
    return 0;
}