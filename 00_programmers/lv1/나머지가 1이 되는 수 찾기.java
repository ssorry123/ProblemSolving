class Solution {
    public int solution(int n) {
        int answer = 0;
        
        // n = a * x + 1 // 가장 작은 x 찾기
        // n-1 = a * x // 1로 나누는 것은 예외
        // x는 2부터 시작
        n = n - 1;
        for(answer = 2; answer <= n; ++answer){
            if(n % answer == 0){
                break;
            }
        }
        
        
        return answer;
    }
}