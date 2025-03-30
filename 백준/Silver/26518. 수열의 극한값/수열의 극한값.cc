#include <bits/stdc++.h>

using namespace std;


int main() {
    int b, c, a1, a2; cin >> b >> c >> a1 >> a2;
    double past_value, value;
    past_value = (double)a1/a2;

    cout << fixed;   //출력형식 제한
    cout.precision(6);

    while (true) {
        value = c/past_value + b;

        if(float(value) == float(past_value)) {
            cout << value;
            break;
        }
        past_value = value;
    }
    
    return 0;
}