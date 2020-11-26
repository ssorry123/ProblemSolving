import java.math.BigInteger;

class Solution {

    // 최대 공약수
    private static int getGcd(int a, int b) {
        BigInteger ba = BigInteger.valueOf(a); // int -> BigInteger
        BigInteger bb = BigInteger.valueOf(b); // int -> BigInteger
        BigInteger gcd = ba.gcd(bb); // gcd 구하기
        return gcd.intValue(); // int로 변환 후 반환
    }

    public int[] solution(int n, int m) {
        int[] answer = { 0, 0 };

        // 최대 공약수
        answer[0] = getGcd(n, m);

        // 최대 공배수 구하기
        answer[1] = answer[0] * (n / answer[0]) * (m / answer[0]);

        return answer;
    }
}