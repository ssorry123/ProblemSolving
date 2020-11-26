import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {

        // greedy 알고리즘
        Arrays.sort(d); // 기본 오름차순 정렬

        int idx = 0;
        // 예산이 남아있고, 예산을 지급할 부서에 예산을 줄 수 있다면
        while (idx < d.length && budget > 0 && d[idx] <= budget) {
            budget -= d[idx];
            ++idx;
            // System.out.println(budget + " " + idx);
        }

        return idx;
    }
}