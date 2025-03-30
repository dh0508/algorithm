#include <iostream>
using namespace std;

int gcd(int a,int b)//유클리드 호제법
{
    if(b==0)return a;
    return gcd(b,a%b);
}
int T; //테스트케이스의 개수
int a; //최소공배수

int main()
{
    scanf("%d",&T);
    while(T--) //T번 실행
    {
        scanf("%d",&a);
        int ans=1; //서로소인 자연수 쌍의 개수
//어떤 자연수이던 (1,a)는 반드시 서로소인 자연수 쌍에 포함되기 때문에 1로 초기화

        for(int i=2;i*i<=a;i++) //ans를 1로 초기화한 것과 같은 이유로 i=2부터 시작
//예를 들어 a를 30이라 했을 때 서로소인 자연수 쌍이(2,15)와 (15,2) 두 가지 경우가 들어가면
//안 되기 때문에 i*i<=a가 될 때까지만 반복
        {
                if(a%i==0)
                {
                    if(gcd(i,a/i)==1)ans++;
                } //a%i가 0이고 gcd(i,a/i)가 1이라면 ans에 1을 더한다.
        }
        printf("%d\n",ans);
    }
    return 0;
}