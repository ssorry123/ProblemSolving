import java.util.*;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */

class Item implements Comparable<Item> {
    public Integer key; // 점수
    public Integer cnt; // 빈도

    Item(int key) {
        this.key = key;
        cnt = 0;
    }

    // 큰것이 먼저 오게
    @Override
    public int compareTo(Item item) {
        if (cnt != item.cnt)
            return -cnt.compareTo(item.cnt);
        else
            return -key.compareTo(item.key);
    }
}

class Solution {
    public static int solution(int[] scores) {
        List<Item> list = new ArrayList<>();
        // 초기화
        for (int i = 0; i <= 100; ++i) {
            list.add(i, new Item(i));
        }

        // 데이터 입력
        for (int score : scores) {
            ++list.get(score).cnt;
        }

        // 정렬
        Collections.sort(list);

        // 정답 리턴
        return list.get(0).key;
    }

    public static void main(String args[]) throws Exception {

        /*
         * 표준입력 System.in 으로부터 스캐너를 만들어 데이터를 읽어옵니다.
         */
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        int studentNum = 1000;
        for (int test_case = 1; test_case <= T; test_case++) {
            int testNumber = sc.nextInt();
            int answer;

            int[] scores = new int[studentNum];
            for (int i = 0; i < studentNum; ++i) {
                scores[i] = sc.nextInt();
            }

            answer = solution(scores);
            System.out.printf("#%d %d\n", testNumber, answer);
        }

        sc.close();
    }
}