import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static Deque<Integer> dq;
    private static boolean dqState = true;

    public static int dqPop() {
        // 정방향이면 앞에서 부터 빼고
        // 역방향이면 뒤부터 뺀다
        if (dqState) {
            return dq.removeFirst();
        } else {
            return dq.removeLast();
        }
    }

    public static boolean solution(String p) throws IOException {
        // true이면 정상 상태, false이면 뒤집힌 상태

        // 주어진 명령을 실행한다
        for (int i = 0; i < p.length(); ++i) {
            char c = p.charAt(i);

            // 맨 앞 삭제 명령인 경우
            if (c == 'D') {
                // 비어있으면 오류이다
                if (dq.isEmpty()) {
                    return false;
                }
                // 정방향인 경우, 앞에서 제거
                if (dqState) {
                    dq.removeFirst();
                    // 역방향인 경우, 뒤에서 제거
                } else {
                    dq.removeLast();
                }
                // 뒤집기 명령인 경우
            } else if (c == 'R') {
                // true면 false로 바꾼다
                dqState = dqState ? false : true;
            }
        }
        return true;
    }

    // 정수로 변환 가능한가?
    public static boolean isInteger(String s) {
        try {
            Integer.parseInt(s);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        int testCase = Integer.valueOf(br.readLine());

        // 입력 데이터 가공
        for (int t = 0; t < testCase; ++t) {
            // 입력 받기
            String p = br.readLine();
            int size = Integer.valueOf(br.readLine());
            String strArr = br.readLine();

            // 문자열 -> 배열로 변환후 dq에 저장
            dq = new ArrayDeque<>(); // 디큐 사용, 초기화
            dqState = true; // 초기화

            // 양쪽 괄호 제거
            strArr = strArr.substring(1, strArr.length() - 1);

            String[] tmp = strArr.split(",");
            for (String s : tmp) {
                // 정수로 변환 가능하면
                if (Main.isInteger(s)) {
                    int val = Integer.valueOf(s);
                    dq.addLast(val);
                }
            }

            // 실행
            boolean ret = Main.solution(p);

            // 결과 출력
            if (!ret) {
                bw.write("error\n");
                continue;
            }

            int n = dq.size();
            if (n == 0) {
                bw.write("[]\n");
            } else {
                bw.write("[");
                for (int i = 0; i < n - 1; ++i) {
                    bw.write(dqPop() + ",");
                }
                bw.write(dqPop() + "]\n");
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
