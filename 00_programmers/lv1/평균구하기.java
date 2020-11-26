class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        
        int sum = 0;
        for (int val : arr) {
            sum += val;
        }
        
        answer = sum / (double)arr.length;
        
        return answer;
    }
}