#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <cmath>

using namespace std;

typedef long long item;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // A : 고정 지출
    // B : 노트북 한대 생산 비용
    // C : 노트북 판매 가격
    item A, B, C;
    cin >> A >> B >> C;

    // x : 판매량
    // C*x > A + B*x
    // x > A / (C-B) ,, C-B > 0

    if (C - B <= 0) {
        cout << -1;
    }
    else {
        cout << (item)floor(A / (C - B)) + 1;
    }

    return 0;
}
