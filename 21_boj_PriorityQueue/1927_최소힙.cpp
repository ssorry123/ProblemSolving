#include <queue>
#include <cstdio>
#include <iostream>

using namespace std;

// cc의 pq는 기본 max힙이다
// 최소 값을 뽑을 때는 부호를 바꾼 후 저장해보자
// 가장 큰 값은 가장 작은 값이 되어, 가장 나중에 나오게 된다
priority_queue<int> pq;
int main() {
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        int buf;
        scanf("%d", &buf);
        // 최대 힙의 가장 작은 값을 출력하는 부분
        if (buf == 0) {
            if (pq.empty()) {
                printf("0\n");
                continue;
            }
            printf("%d\n", -pq.top());
            pq.pop();
        }
        // 최대 힙에 삽입하는 부분
        else {
            pq.push(-buf);
        }
    }

    return 0;
}
