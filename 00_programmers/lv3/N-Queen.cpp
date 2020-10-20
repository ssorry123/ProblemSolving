#include <string>
#include <vector>

using namespace std;

typedef vector<vector<int> > vvi;

bool check(int row, int col, vvi& chess) {
    // col 검사
    for (int r = 0; r < chess.size(); ++r)
        if (chess[r][col] == 1)
            return false;
    // row 검사
    for (int c = 0; c < chess.size(); ++c)
        if (chess[row][c] == 1)
            return false;
    // 대각선 검사
    int dr[] = { -1, -1, 1, 1 };
    int dc[] = { -1, 1, -1, 1 };
    for (int i = 0; i < 4; ++i) {
        int diff = 1;
        while (true) {
            int nr = row + dr[i] * diff, nc = col + dc[i] * diff;
            // 맵을 벗어나면 검사하지 않는다
            if (nr < 0 || nr >= chess.size() || nc < 0 || nc >= chess.size())
                break;
            // 퀸이있다면 false 반환
            if (chess[nr][nc] == 1)
                return false;
            ++diff;
        }
    }

    return true;
}

void queen(int row, vvi& chess, int* answer) {
    if (row == chess.size()) {
        ++(*answer);
        return;
    }

    for (int col = 0; col < chess.size(); ++col) {
        // 퀸을 놓을 수 있으면
        if (check(row, col, chess)) {
            chess[row][col] = 1;            // 퀸 놓기
            queen(row + 1, chess, answer);  // 다음 줄에 퀸놓으러 가기
            chess[row][col] = 0;            // 퀸 빼기
        }
    }

}

int solution(int n) {
    int answer = 0;
    vvi chess(n, vector<int>(n, 0));

    queen(0, chess, &answer);

    return answer;
}