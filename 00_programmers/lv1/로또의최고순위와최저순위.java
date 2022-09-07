class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        // 알 수 없는 0은 최소 0개, 최대 6개
        // 
        int cnt0 = 0; // 0의 개수
        int corrCnt = 0; // 0이 아니고 맞춘 개수
        
        for(int lotto : lottos){
            // 알수 없는 번호일 경우
            if(lotto == 0){
                ++cnt0;
                continue;
            }
            // 알수 있는 번호일 경우, 당첨번호와 일치하는지 확인
            for(int win_num : win_nums){
                if(lotto == win_num){
                    ++corrCnt;
                }
            }
        }
        // 0. 다 0인경우는 답이 정해져있음.
        if(cnt0 == 6){
            return new int[]{1,6};
        }
        ///// 0 이 하나라도 있는 경우
        // 1. 최고순위
        /// 0이 다 맞았을 경우 맞춘 개수
        int maxCorrCnt = corrCnt + cnt0; 
        /// 0이 다 틀렸을 경우 맞춘 개수
        int minCorrCnt = corrCnt;
        
        int maxRanking = maxCorrCnt >= 2 ? 7-maxCorrCnt : 6;
        int minRanking = minCorrCnt >= 2 ? 7-minCorrCnt : 6;
        
        return new int[]{maxRanking, minRanking};
    }
}