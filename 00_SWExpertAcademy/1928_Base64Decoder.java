import java.util.*;

class Solution {

    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        sc.nextLine();

        for (int test_case = 1; test_case <= T; test_case++) {
            String str = sc.nextLine(); // 64로 인코딩 된 것
            // 자바에는 Base64 라이브러리가 있다.
            str = new String(Base64.getDecoder().decode(str));

            System.out.printf("#%d %s\n", test_case, str);

        }

        sc.close();
    }
}