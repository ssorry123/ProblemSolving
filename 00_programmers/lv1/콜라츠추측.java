class Solution {
    // num은 원래 int지만, *3 + 1 하다보면 오버플로우 발생할 수 있으므로
    // long으로 선언한다
    public int solution(long num) {
        int answer = 0;

        // 항상 예외 처리를 해줄 것
        if (num == 1)
            return 0;

        for (answer = 0; answer < 500; ++answer) {
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num = num * 3 + 1;
            }

            if (num == 1)
                break;
        }

        if (num != 1)
            return -1;
        return answer + 1;
    }
}