import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
// import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        
        // Scanner sc = new Scanner(System.in);
        // int N = sc.nextInt();
        // sc.nextLine(); // 개행 문자 제거
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.valueOf(br.readLine());

        // dq 라이브러리 사용
        Deque<Integer> dq = new ArrayDeque<>();

        for (int t = 0; t < N; ++t) {
            String[] operation = br.readLine().split(" ");
            String op = operation[0];   // 명령어 추출

            if (op.equals("push_front")) {
                dq.addFirst(Integer.valueOf(operation[1]));

            } else if (op.equals("push_back")) {
                dq.addLast(Integer.valueOf(operation[1]));

            } else if (op.equals("pop_front")) {
                if (dq.isEmpty()) {
                    // System.out.println(-1);
                    bw.write("-1\n");
                    continue;
                }
                // System.out.println(dq.removeFirst());
                bw.write(dq.removeFirst()+"\n");

            } else if (op.equals("pop_back")) {
                if (dq.isEmpty()) {
                    // System.out.println(-1);
                    bw.write("-1\n");
                    continue;
                }
                // System.out.println(dq.removeLast());
                bw.write(dq.removeLast()+"\n");

            } else if (op.equals("size")) {
                // System.out.println(dq.size());
                bw.write(dq.size() + "\n");

            } else if (op.equals("empty")) {
                if (dq.isEmpty()) {
                    bw.write("1\n");
                } else {
                    bw.write("0\n");
                }

            } else if (op.equals("front")) {
                if (dq.isEmpty()) {
                    bw.write("-1\n");
                    continue;
                }
                // System.out.println(dq.getFirst());
                bw.write(dq.getFirst() + "\n");

            } else if (op.equals("back")) {
                if (dq.isEmpty()) {
                    bw.write("-1\n");
                    continue;
                }
                // System.out.println(dq.getLast());
                bw.write(dq.getLast() + "\n");
            } else {

            }
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
