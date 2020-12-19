#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <stack>
#include <cmath>

using namespace std;

// 백준에서는 자료형의 범위도 체크해줘야;;
typedef long long item;
typedef vector<item> vi;


item divideConquer(int left, int right, vi& arr) {
    if (left == right) {
        return arr[left];
    }

    // 두 구간으로 나누고, 최대 넓이를 결과값으로
    int mid = (left + right) / 2;
    item ret = max(divideConquer(left, mid, arr), divideConquer(mid + 1, right, arr));

    // 두 구간을 걸치는 경우도 고려(핵심)
    item width = 2;
    item height = min(arr[mid], arr[mid + 1]);
    ret = max(ret, width * height);

    // 양쪽 중에서 하나를 고를때, 항상 높이가 더 높은 것을 선택한다
    int le = mid - 1, ri = mid + 2; // le, ri는 후보임
    while (left <= le || ri <= right) {
        item leH, riH;
        if (left > le)
            leH = -1;
        else leH = arr[le];
        if (ri > right)
            riH = -1;
        else riH = arr[ri];

        if (leH > riH) {
            height = min(height, leH);
            --le;
            ++width;
        }
        else if (leH < riH) {
            height = min(height, riH);
            ++ri;
            ++width;
        }
        else {
            height = min(height, riH);
            ++ri; --le;
            width += 2;
        }
        ret = max(ret, width * height);
    }

    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    while (n != 0) {
        vi arr(n);
        for (int i = 0; i < n; ++i)
            cin >> arr[i];
        item answer = divideConquer(0, n - 1, arr);
        cout << answer << "\n";
        cin >> n;
    }

    return 0;
}