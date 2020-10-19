#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> arr;
vector<int> cache;

// idx부터 시작했을때 합이 가장 큰 증가 부분수열의 합을 구한다
int func(int idx) {
    if (cache[idx] != -1)
        return cache[idx];


    int tmp = 0;
    for (int next = idx + 1; next < arr.size(); ++next) {
        if (arr[next] > arr[idx]) {
            tmp = max(tmp, func(next));
        }
    }

    // 자기 자신값 + idx 이후의 증가부분수열의 최대값
    cache[idx] = arr[idx] + tmp;
    return cache[idx];
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // 배열 초기화 후 입력받기
    int N, tmp;
    cin >> N;
    arr.clear();
    for (int i = 0; i < N; ++i) {
        cin >> tmp;
        arr.push_back(tmp);
    }

    // 메모이제이션용 캐시 초기화
    cache.clear();
    cache.resize(N, -1);

    // 답 구하기
    int answer = 0;
    for (int i = 0; i < N; ++i) {
        answer = std::max(answer, func(i));
    }

    cout << answer << endl;

    return 0;
}