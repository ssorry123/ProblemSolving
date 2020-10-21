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

    item A, B, V;
    cin >> A >> B >> V;

    // 하루에 A만큼 올라가고, 잘때 B만큼 떨어진다
    // V에 도달하면 잠을 자지 않는다
    // (A-B) * (day-1) + A * (1) >= V 인 day를 찾는다

    // day >= (V-B)/(A-B)
    item a = V - B;
    item b = A - B;

    if (a % b == 0)
        cout << (item)(a / b);
    else
        cout << (item)floor(a / b) + 1;
    
    
    return 0;
}
