import java.util.Arrays;
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
public class Solution {
    public static void main(String args[]) throws Exception {
        /*
         * 표준입력 System.in 으로부터 스캐너를 만들어 데이터를 읽어옵니다.
         */
        Scanner sc = new Scanner(System.in);
        int T = 10;

        /*
         * 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
         */
        // System.out.println("Hello world");

        for (int test_case = 1; test_case <= T; test_case++) {
            // 빌딩들의 사이즈 입력 받기
            int size = sc.nextInt(); // 배열 크기 입력
            int[] arr = new int[size];
            for (int i = 0; i < size; ++i) {
                arr[i] = sc.nextInt();
            }
            int ret = 0;
            // 양쪽 끝 두 지역은 건물이 없다
            for (int bIdx = 2; bIdx < size - 2; ++bIdx) {
                // 양 쪽 건물중 가장 높은 건물 조사
                int leftMax = Math.max(arr[bIdx - 2], arr[bIdx - 1]);
                int rightMax = Math.max(arr[bIdx + 1], arr[bIdx + 2]);
                int meMax = Math.max(leftMax, rightMax);
                int tmpRet = arr[bIdx] - meMax;
                if (tmpRet <= 0) {
                    continue;
                }
                ret += tmpRet;
            }

            System.out.printf("#%d %d\n", test_case, ret);

        }
    }
}