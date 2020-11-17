#include <string>
#include <iostream>
#include <vector>

using namespace std;

typedef struct _visited {
    int ax;
    int ay;
    int bx;
    int by;
}Visited;

// 구조체 비교 함수
bool same(Visited& a, Visited& b) {
    if (a.ax == b.ax)
        if (a.ay == b.ay)
            if (a.bx == b.bx)
                if (a.by == b.by)
                    return true;
    return false;
}

// 해당 경로를 방문한 적이 있는가?
bool passed(Visited check, vector<Visited>& visited) {
    for (int i = 0; i < visited.size(); ++i) {
        if (same(check, visited[i]))
            return true;
    }
    return false;
}

int solution(string dirs) {
    int answer = 0;

    const int map_size = 5;

    // 방문한 간선 기록
    vector<Visited> visited;
    // 초기 위치
    int x = 0, y = 0;

    // 순서대로 명령 수행
    for (int i = 0; i < dirs.length(); ++i) {
        char op = dirs[i];

        int tx = x, ty = y; // 다음 위치
        if (op == 'U') ++ty;
        else if (op == 'D') --ty;
        else if (op == 'R') ++tx;
        else if (op == 'L') --tx;
        else {}

        // 맵을 벗어나는 명령이면
        if (tx > map_size) continue;
        if (tx < -map_size) continue;
        if (ty > map_size) continue;
        if (ty < -map_size) continue;

        // 위치 이동
        // 모든 길은 두가지로 표현된다
        // 방문하지 않은 길이라면
        if (!passed({ tx, ty, x, y }, visited) && !passed({ x, y, tx, ty }, visited)) {
            // 방문한 길에 추가
            visited.push_back({ x, y, tx, ty });
            visited.push_back({ tx, ty, x, y });
            // 정답 올리기
            ++answer;
        }
        // 위치 이동
        x = tx;
        y = ty;

    }

    return answer;
}

int main() {
    solution("ULURRDLLU");
    return 0;
}
