#include <iostream>
#include <string>

using namespace std;

using uint128 = __uint128_t; // 128비트 정수 자료형

// __uint128_t를 문자열로 변환하는 함수
string uint128_to_string(uint128 num) {
    if (num == 0) return "0";
    string result;
    while (num > 0) {
        result = char('0' + (num % 10)) + result;
        num /= 10;
    }
    return result;
}

int main() {
    int n, m;
    cin >> n >> m;
    
    m = min(m, n - m);
    uint128 result = 1;

    for (int i = 0; i < m; i++) {
        result = result * (n - i) / (i + 1);
    }

    cout << uint128_to_string(result) << endl;
    return 0;
}