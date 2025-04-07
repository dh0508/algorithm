#include <bits/stdc++.h>

using namespace std;

int main() {
    int A, P; cin >> A >> P;
    vector<long long>v;
    v.push_back(A);
    while (true) {
        string strA = to_string(A);
        int tmp = 0;
        for (int i=0; i<strA.size(); i++) {
            tmp += pow(strA[i] - '0', P);
        }
        if (find(v.begin(), v.end(), tmp) != v.end()) {
            cout << distance(v.begin(), find(v.begin(), v.end(), tmp));
            break;
        }
        else {
            v.push_back(tmp);
            A = tmp;
        }

    }


    return 0;
}