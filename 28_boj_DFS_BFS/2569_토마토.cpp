#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define MAX 100
// High, Row, Col
int adj[MAX][MAX][MAX];
int N, M, H;	// row수, col수, 높이
int cnt_0 = 0;	// 익지 않은 토마토 수

typedef struct _XYZ {
    int r;
    int c;
    int h;
}XYZ;
XYZ make_XYZ(int r, int c, int h);

bool check(XYZ& xyz);

// 레벨이 day인 토마토(r, c) 근처에 있는 안 익은 토마토들을
// 익은 토마토로 바꾸고, 레벨이 day+1인 토마토를 저장하는 큐에 추가한다
void bfs(XYZ& xyz, queue<XYZ>& q) {
    int arr[6][3] =
    {
        {1, 0, 0},	// 아래
        {-1, 0, 0},	// 위
        {0, 1, 0},	// 오른쪽
        {0, -1, 0},	// 왼쪽
        {0, 0, -1},	// 아래층
        {0, 0, 1}	// 위층
    };
    int r = xyz.r, c = xyz.c, h = xyz.h;

    for (int i = 0; i < 6; ++i) {
        int next_r, next_c, next_h;
        next_r = r + arr[i][0];
        next_c = c + arr[i][1];
        next_h = h + arr[i][2];
        XYZ temp = make_XYZ(next_r, next_c, next_h);
        // 익게 만들 수 있는 토마토인 경우
        if (check(temp)) {
            adj[next_h][next_r][next_c] = 1;	// 익게 만든다
            q.push(temp);						// 큐에 추가
            --cnt_0;							// 익지 않은 토마토 수 제거
        }
    }
}

int main(int argc, char** argv) {
    // col수, row수
    cin >> M >> N >> H;
    int tmp;
    // 0일차에 익어있는 토마토들
    queue<XYZ> q_today;
    for (int h = 0; h < H; ++h)
        for (int r = 0; r < N; ++r)
            for (int c = 0; c < M; ++c) {
                scanf("%d", &tmp);
                adj[h][r][c] = tmp;
                if (tmp == 0)
                    ++cnt_0;
                if (tmp == 1)
                    q_today.push(make_XYZ(r, c, h));
            }

    // 모든 토마토가 익어있다면(익지 않은 토마토가 한개도 없다면)
    if (cnt_0 == 0)
        cout << 0 << endl;
    else {
        int day = 0;
        while (true) {
            // day+1 큐 생성
            queue<XYZ> q_tomorrow;
            while (!q_today.empty()) {
                // today에 익어있는 토마토들
                XYZ me = q_today.front();
                q_today.pop();
                int me_r = me.r, me_c = me.c, me_h = me.h;
                // 자신 주변의 토마토들을 익게 만든 후, tomorrow 큐에 추가한다
                bfs(me, q_tomorrow);
            }
            // tomorrow에 아무런 토마토를 만들지 못한 경우
            if (q_tomorrow.empty())
                break;
            // 다음날!
            q_today = q_tomorrow;
            ++day;
        }
        if (cnt_0 > 0)
            cout << -1 << endl;
        else
            cout << day << endl;
    }

    return 0;
}

bool check(XYZ& xyz) {
    int r = xyz.r, c = xyz.c, h = xyz.h;
    if (r >= N || r < 0 || c >= M || c < 0 || h >= H || h < 0)
        return false;
    // 처음부터 익지 않은 토마토인 경우
    if (adj[h][r][c] == 0)
        return true;
    // 그 외 모든 경우 false
    return false;
}
XYZ make_XYZ(int r, int c, int h) {
    XYZ ret;
    ret.r = r;
    ret.c = c;
    ret.h = h;
    return ret;
}