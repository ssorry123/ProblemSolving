class Solution {
    int MOD = 20170805;

    class Flow {
        int right;
        int down;
        int total;

        Flow(int right, int down, int total) {
            this.right = right;
            this.down = down;
            this.total = total;
        }
    }

    public void printArr(Flow[][] flow) {
        for (int r = 0; r < flow.length; ++r) {
            for (int c = 0; c < flow[0].length; ++c) {
                System.out.print(flow[r][c].down + "," + flow[r][c].right + "(" + flow[r][c].total + ") ");
            }
            System.out.println();
        }
    }

    // DP로 푼다
    public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        // 맵 생성후 초기화
        Flow[][] flow = new Flow[m][n];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                flow[r][c] = new Flow(0, 0, 0);
        flow[0][0].down = flow[0][0].right = flow[0][0].total = 1;

        // 세로줄 초기화
        for (int r = 1; r < m; ++r) {
            int val = cityMap[r][0];
            Flow tmp = flow[r][0];

            // 통행 불가지역인 경우
            if (val == 1) {
                tmp.down = tmp.right = tmp.total = 0;
            }
            // 일방통행인 경우
            else if (val == 2) {
                if (flow[r - 1][0].down == 1) {
                    tmp.total = tmp.down = 1;
                }
            }
            // 그냥 지역인 경우
            else {
                if (flow[r - 1][0].down == 1) {
                    tmp.total = tmp.down = tmp.right = 1;
                }
            }
        }

        // 가로줄 초기화
        for (int c = 1; c < n; ++c) {
            int val = cityMap[0][c];
            Flow tmp = flow[0][c];

            // 통행 불가지역인 경우
            if (val == 1) {
                tmp.total = tmp.down = tmp.right = 0;

            }
            // 일방통행인 경우
            else if (val == 2) {
                if (flow[0][c - 1].right == 1) {
                    tmp.total = tmp.right = 1;
                }

            }
            // 그냥 지역인 경우
            else {
                if (flow[0][c - 1].right == 1) {
                    tmp.total = tmp.down = tmp.right = 1;
                }
            }
        }
        // print
        // printArr(flow);

        // DP
        for (int r = 1; r < m; ++r) {
            for (int c = 1; c < n; ++c) {
                int meVal = cityMap[r][c];
                // 통행 불가지역 패스
                if (meVal == 1)
                    continue;

                int up = 0; // 위에서 오는 값
                int left = 0; // 왼쪽에서 오는 값
                int upVal = cityMap[r - 1][c]; // 윗지역 특성
                int leftVal = cityMap[r][c - 1]; // 왼쪽 지역 특성

                // 특성에 따라 오는 값이 다르다
                // 윗 지역이 그냥 지역이었다면
                if (upVal == 0) {
                    up = flow[r - 1][c].total;
                }
                // 윗 지역이 일방통행 지역이었다면
                else if (upVal == 2) {
                    up = flow[r - 1][c].down;
                }
                // 윗 지역이 통행 불가 지역이었다면, 올 것이 없음
                else if (upVal == 1) {
                    up = 0;
                }

                if (leftVal == 0) {
                    left = flow[r][c - 1].total;
                } else if (leftVal == 2) {
                    left = flow[r][c - 1].right;
                } else if (leftVal == 1) {
                    left = 0;
                }

                // 나는 어떤 지역인가, 어떤 특성을 가지게 되는가
                // 그냥 지역이면
                Flow me = flow[r][c];
                if (meVal == 0) {
                    me.total = (me.total + up + left) % MOD;
                    me.down = (me.down + up + left) % MOD;
                    me.right = (me.right + up + left) % MOD;
                }
                // 일방통행 지역이면
                else if (meVal == 2) {
                    me.total = (me.total + up + left) % MOD;
                    me.down = (me.down + up) % MOD; // 내려가는 플로우는 위에서 오는 것만 가능
                    me.right = (me.right + left) % MOD; // 오른쪽 플로우는 왼쪽에서 오는 것만 가능
                }

            }
        }

        // System.out.println();
        // printArr(flow);

        return flow[m - 1][n - 1].total;
    }
}
