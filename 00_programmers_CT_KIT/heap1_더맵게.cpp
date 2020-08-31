#include <string>
#include <vector>
#include <queue>

using namespace std;

// 작은것이 우선순위가 높게
struct comp {
    bool operator()(int& a, int& b) {
        return a > b;
    }
};
priority_queue<int, vector<int>, comp> pq;
int solution(vector<int> scoville, int K) {
    int answer = 0;
    for (int i = 0; i < scoville.size(); ++i) {
        pq.push(scoville[i]);
    }

    // 새로운 음식의 맵기만드는 방법은 정해져있으므로
    // 만들다가 가장 맵기가 작은 음식이 K보다 클때가 최소 횟수
    int ret = 0;
    // 가장 안매운 음식이 K보다 작을 경우 두 음식을 합쳐본다
    while (pq.top() < K) {
        // 한번 섞을때마다 음식의 개수가 하나씩 줄어든다
        // 음식이 하나남았는데도 이 반복문을 탈출하지 못한다면 만들 수 없는 경우이다
        if (pq.size() == 1) {
            ret = -1;
            break;
        }

        int a = pq.top();
        pq.pop();
        int b = pq.top();
        pq.pop();
        pq.push(a + 2 * b);
        ++ret;
    }

    answer = ret;

    return answer;
}