#include <vector>
#include <iostream>
#include <algorithm>

// cmath에 정의된 여러 상수를 이용하기 위해서
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

bool comp(double a, double b) {
    // 차이가 0.000001이하라면 같다고 판정
    if (abs(a - b) < 0.000001)
        return true;
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int testCase;
    cin >> testCase;

    for (int t = 0; t < testCase; ++t) {
        double x1, y1, x2, y2, r1, r2;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        double d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));

        // d==0
        if (comp(d, 0)) {
            if (comp(r1, r2))
                cout << "-1\n"; // 무한대
            else
                cout << "0\n";  // 존재할 수 없음
        }
        // d == r1+r2
        else if (comp(d, r1 + r2)) {
            cout << "1\n";  // 정확히 한곳
        }
        // d > r1 + r2
        else if (d > r1 + r2) {
            cout << "0\n";  // 존재할 수 없음
        }
        // d < r1 + r2
        else {
            if (comp(r1, r2)) {
                cout << "2\n";
                continue;
            }
            if (r1 > r2) {
                double tmp = r1;
                r1 = r2;
                r2 = tmp;
            }
            // 작은 원과 큰 원이 한 점에서 만나는 경우
            if (comp(d + r1, r2)) {
                cout << "1\n";
            }
            // 큰원안에 작은원이 있고 한점도 만나지 않는 경우
            else if (d + r1 < r2) {
                cout << "0\n";
            }
            // 큰원과 작은원이 두점씩 겹치는 경우
            else {
                cout << "2\n";
            }
        }
    }

    return 0;
}
