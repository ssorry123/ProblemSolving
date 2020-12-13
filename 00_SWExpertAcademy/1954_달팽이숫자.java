import java.util.*;

class Solution {

    public static void arrPrint(int[][] arr) {
        for (int r = 0; r < arr.length; ++r) {
            for (int c = 0; c < arr[r].length; ++c) {
                System.out.printf("%d ", arr[r][c]);
            }
            System.out.println();
        }
    }

    public static void solution(int n) {
        // 자동 초기화 0
        int[][] map = new int[n][n];
        // arrPrint(map);

        int r = 0;
        int c = 0;
        // 순서 == right, down, left, up
        int[][] direct = new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
        int directIdx = 0;
        int N = n * n;
        int i = 1;

        while (i <= N) {
            map[r][c] = i; // 쓴다

            // r,c를 갱신한다
            int tmpR = r + direct[directIdx][0];
            int tmpC = c + direct[directIdx][1];

            // 만약 밖으로 나가거나, 이미 기록한 위치라면 방향을 튼다
            if (tmpR < 0 || tmpC < 0 || tmpR >= n || tmpC >= n || map[tmpR][tmpC] != 0) {
                directIdx = (directIdx + 1) % direct.length;
                tmpR = r + direct[directIdx][0];
                tmpC = c + direct[directIdx][1];
            }

            r = tmpR;
            c = tmpC;
            ++i;
        }

        arrPrint(map);
    }

    public static void main(String args[]) throws Exception {
        /*
         * 아래의 메소드 호출은 앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다. 여러분이 작성한 코드를
         * 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후, 이 코드를 프로그램의 처음 부분에 추가하면 이후 입력을 수행할 때
         * 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다. 따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 메소드를 사용하셔도 좋습니다.
         * 단, 채점을 위해 코드를 제출하실 때에는 반드시 이 메소드를 지우거나 주석 처리 하셔야 합니다.
         */
        // System.setIn(new FileInputStream("res/input.txt"));

        /*
         * 표준입력 System.in 으로부터 스캐너를 만들어 데이터를 읽어옵니다.
         */
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        /*
         * 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
         */

        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.printf("#%d\n", test_case);
            solution(sc.nextInt());
        }

        sc.close();
    }
}