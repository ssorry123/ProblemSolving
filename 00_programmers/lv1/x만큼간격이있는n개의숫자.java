import java.util.ArrayList;

class Solution {
    public long[] solution(long x, int n) {

        // 객체 생성시 생략 가능
        ArrayList<Long> ret = new ArrayList<>();
        int count = 0;
        long val = x;
        while (count < n) {
            ret.add(val);
            val += x;
            ++count;
        }

        long[] answer = new long[ret.size()];
        for (int i = 0; i < answer.length; ++i) {
            answer[i] = ret.get(i).longValue(); // Long -> long 변환
        }

        return answer;
    }
}