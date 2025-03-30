#include <bits/stdc++.h>

using namespace std;

int main() {

    string name; cin >> name;
    sort(name.begin(), name.end());
    char temp = name[0]; int tempcnt = 1; int oddcnt = 0; char oddchar = 0;
    for (int i=1; i<name.size(); i++) {
        if (temp == name[i]) {
            tempcnt += 1;
            temp = name[i];
        }
        else {
            if (tempcnt % 2 != 0) {
                oddcnt += 1;
                oddchar = name[i-1];
            }
            tempcnt = 1;
            temp = name[i];

        }
    }
    if (tempcnt % 2 != 0) {
        oddcnt += 1;
        oddchar = name[name.size()-1];

    }

    if (oddcnt > 1) {
        cout << "I'm Sorry Hansoo";
        return 0;
    }


    if (oddchar == 0) {
        for (int i=0; i<name.size(); i+=2) {
            cout << name[i];
        }
        for (int i=name.size()-1; i>=0; i-=2) {
            cout << name[i];
        }
    }
    else {
        name.erase(name.find(oddchar), 1);
        for (int i=0; i<name.size(); i+=2) {
            cout << name[i];
        }
        cout << oddchar;
        for (int i=name.size()-1; i>=0; i-=2) {
            cout << name[i];
        }
    }

    return 0;
}
