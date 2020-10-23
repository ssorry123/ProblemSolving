#include <string>
#include <vector>

using namespace std;

vector<vector<int>> answer;
void hanoi(int n, int from, int assist, int to) {
    if (n == 1) {
        // 한개면, 그냥 from에서 to로 옮긴다
        answer.push_back({ from, to });
        return;
    }

    hanoi(n - 1, from, to, assist); // n-1개를 assist로 옮긴다
    answer.push_back({ from, to }); // 가장 큰 원판을 목적지로 옮긴다
    hanoi(n - 1, assist, from, to); // assist에 있는 n-1개 원판을 목적지로 옮긴다

}

vector<vector<int>> solution(int n) {
    answer.clear();
    // 1에있는 n개의 원반을, 
    // 2를 이용하여
    // 모두 3으로 옮기자
    hanoi(n, 1, 2, 3);

    return answer;
}

int main() {

    solution(2);

    return 0;
}