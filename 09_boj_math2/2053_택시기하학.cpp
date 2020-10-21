#include <vector>
#include <iostream>
#include <algorithm>

// cmath에 정의된 여러 상수를 이용하기 위해서
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int R;
    cin >> R;
   
    cout << fixed;  // 소수점을 고정해서 표현
    cout.precision(6);  // 소수부분 6자리 고정
    cout << pow(R, 2) * M_PI << endl;
    cout << (double)pow(2 * R, 2) / 2;

    return 0;
}
