#include <iostream>
#include <algorithm>
using namespace std;

// 멘토와 멘티 정보를 저장하는 배열
pair<string, string> arr[100001];

// 비교 함수
bool compare(pair<string, string> a, pair<string, string> b) {
    if (a.first == b.first) {
        return a.second > b.second; // 멘티 이름은 내림차순
    }
    return a.first < b.first; // 멘토 이름은 오름차순
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n; // 멘토-멘티 쌍의 수
    cin >> n;

    // 입력 받기
    for (int i = 0; i < n; i++) {
        cin >> arr[i].first >> arr[i].second;
    }

    // 정렬
    sort(arr, arr + n, compare);

    // 출력
    for (int i = 0; i < n; i++) {
        cout << arr[i].first << ' ' << arr[i].second << '\n';
    }

    return 0;
}
