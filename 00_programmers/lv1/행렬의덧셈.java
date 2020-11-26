class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];

        for (int r = 0; r < arr1.length; ++r) {
            for (int c = 0; c < arr1[0].length; ++c) {
                answer[r][c] = arr1[r][c] + arr2[r][c];
            }
        }

        return answer;
    }
}