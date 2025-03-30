#include <stdio.h>
#include <math.h>

int main() {
    double L, A, B, C, D;
    scanf("%lf", &L);
    scanf("%lf", &A);
    scanf("%lf", &B);
    scanf("%lf", &C);
    scanf("%lf", &D);

    int result = (int)L - fmax(ceil(A / C), ceil(B / D));
    printf("%d", result); 
}
