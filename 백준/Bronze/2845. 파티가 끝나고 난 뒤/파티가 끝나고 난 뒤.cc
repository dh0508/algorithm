#include <iostream>

using namespace std;

int main() {
    int L, P;
    int l[5];
    scanf("%d %d", &L, &P);
    scanf("%d %d %d %d %d", &l[0], &l[1], &l[2], &l[3], &l[4]);
    for (int i = 0; i < 5; i++) {
        printf("%d ", l[i] - (L*P));
    }
    return 0;
}