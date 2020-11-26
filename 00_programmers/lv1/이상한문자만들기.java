class Solution {
    public String solution(String s) {
        String answer = "";

        // 홀수 인덱스 -> 대문자
        // 짝수 인덱스 -> 소문자

        int idx = -1;
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);

            // 공백인 경우, 그냥 추가
            // 새로운 단어 입력 대기
            if (c == ' ') {
                idx = -1;
                answer += " ";
                continue;
            }

            // 단어 별로 대문자, 소문자
            ++idx;
            if (idx % 2 == 0) {
                answer += String.valueOf(c).toUpperCase();
            } else {
                answer += String.valueOf(c).toLowerCase();
            }

        }

        return answer;
    }
}