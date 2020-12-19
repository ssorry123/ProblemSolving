#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 수는 1~10000까지의 수
    vector<int> counting(10001, 0);
    int N;
    cin >> N;
    // 카운팅 O(n)
    for (int i = 0; i < N; ++i) {
        int val;
        cin >> val;
        ++counting[val];
    }
    // 출력
    for (int val = 1; val <= 10000; ++val) {
        int cnt = counting[val];
        for (int i = 0; i < cnt; ++i)
            cout << val << "\n";
    }

    return 0;
}
