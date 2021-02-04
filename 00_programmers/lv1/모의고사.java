import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        
        int[][] supoza = {
            {1, 2, 3, 4, 5},
            {2, 1, 2, 3,  2, 4, 2, 5},
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        
        int[] sum = {0,0,0};
        
        for(int i=0; i<3;++i) {
            int k = 0;
            for(int j=0; j<answers.length; ++j) {
                if(supoza[i][k] == answers[j])
                    ++sum[i];
                k = (k+1) % supoza[i].length;
            }
        }
        
        // 0번~2번중 맞춘 문제수 최대값 구하기
        int max = -1;
        for (int i = 0; i < 3; ++i) {
            int id = -1;
            if (sum[i] > max)
                max = sum[i];
        }

        int cnt = 0;
        for(int i=0;i<3;++i)
            if(sum[i]==max)
                cnt++;
        
        answer = new int[cnt];
        int answerIdx = 0;
        for(int i=0;i<3;++i) {
            if(sum[i]==max)
                answer[answerIdx++] = i+1;
        }
        
        return answer;
    }
}