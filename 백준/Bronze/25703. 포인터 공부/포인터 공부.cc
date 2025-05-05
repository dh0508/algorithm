#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; cin >> N;
    cout << "int a;" << endl;
    for (int i = 1; i <= N; i++) {
        cout << "int ";
        for (int j = 0; j < i; j++) {
            cout << "*";
        }
        if (i == 1) {
            cout << "ptr = &a;" << endl;
        } else if (i == 2) {
            cout << "ptr2 = &ptr;" << endl;
        } else {
            cout << "ptr" << i << " = &ptr" << (i - 1) << ";" << endl;
        }
    }

    return 0;
}