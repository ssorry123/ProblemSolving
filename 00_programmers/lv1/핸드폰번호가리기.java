class Solution {
    public String solution(String phone_number) {
        String answer = "";

        // 보여줄 번호 시작 인덱스
        int idx = phone_number.length() - 4;

        // 가릴 부분은 *로 표시
        for (int i = 0; i < idx; ++i)
            answer += "*";
        
        // 보여줄 부분 붙이기
        answer += phone_number.substring(idx);

        return answer;
    }
}