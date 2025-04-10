#include <bits/stdc++.h>

using namespace std;


bool cmp(const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
    if (get<1>(a) != get<1>(b)) {
        return get<1>(a) > get<1>(b);
    } else {
        return get<2>(a) < get<2>(b);
    }
}

int main() {
    int N, C; cin >> N >> C;
    vector<tuple<int, int, int> > v;

    for (int i = 0; i < N; i++) {
        int num; cin >> num;

        bool found = false;
        for (int j = 0; j < v.size(); j++) {
            if (get<0>(v[j]) == num) {
                get<1>(v[j]) += 1;
                found = true;
                break;
            }
        }

        if (!found) {
            v.push_back(make_tuple(num, 1, i));
        }
    }

    sort(v.begin(), v.end(), cmp);

    for (int i = 0; i < v.size(); i++) {
        int value = get<0>(v[i]);
        int freq = get<1>(v[i]);
        for (int j = 0; j < freq; j++) {
            cout << value << " ";
        }
    }

    cout << "\n";
    return 0;
}