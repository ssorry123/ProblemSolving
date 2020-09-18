#include <queue>
#include <cstdio>
#include <iostream>

using namespace std;

priority_queue<int> pq;
int main() {
    int N;
    scanf("%d", &N);
    
    for (int i = 0; i < N; ++i) {
        int buf;
        scanf("%d", &buf);
        // 최대 힙의 가장 큰 값을 출력하는 부분
        if (buf == 0) {
            if (pq.empty()) {
                printf("0\n");
                continue;
            }
            printf("%d\n", pq.top());
            pq.pop();
        }
        // 최대 힙에 삽입하는 부분
        else {
            pq.push(buf);
        }
    }

    return 0;
}
