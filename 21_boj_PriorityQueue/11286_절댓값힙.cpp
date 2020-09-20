#include <queue>
#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

// 절댓값 힙
struct cmp {
    bool operator() (int& a, int& b) {
        int aSize = abs(a);
        int bSize = abs(b);
        // 절댓값이 다른 경우, 절댓값이 작은 것이 더 큰 우선 순위
        if (aSize != bSize)
            return aSize > bSize;
        // 절댓값이 같은 경우, 그냥 작은 것이 더 큰 우선 순위
        else
            return a > b;
    }
};
priority_queue<int, vector<int>, cmp> pq;
int main() {
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        int buf;
        scanf("%d", &buf);
        // 출력 부분
        if (buf == 0) {
            if (pq.empty()) {
                printf("0\n");
                continue;
            }
            printf("%d\n", pq.top());
            pq.pop();
        }
        // 삽입 부분
        else {
            pq.push(buf);
        }
    }

    return 0;
}
