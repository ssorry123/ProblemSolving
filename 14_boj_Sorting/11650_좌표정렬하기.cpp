#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, int> xy;

bool cmp(xy& a, xy& b) {

    // x순으로 정렬
    if (a.first != b.first)
        return a.first < b.first;
    // y순으로 정렬
    else
        return a.second < b.second;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 입력
    int N;
    cin >> N;
    vector<xy> arr;
    for (int i = 0; i < N; ++i) {
        int x, y;
        cin >> x >> y;
        arr.push_back(make_pair(x, y));
    }

    // 정렬
    sort(arr.begin(), arr.end(), cmp);

    // 출력
    for (int i = 0; i < N; ++i) {
        cout << arr[i].first << " " << arr[i].second << "\n";
    }

    return 0;
}
