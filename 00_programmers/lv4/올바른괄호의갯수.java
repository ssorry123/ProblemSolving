import java.util.*;

// DP 같다.
// DP 정답만 보면 깔끔하다.

// n은 최대 14 -> 최열림닫힘괄호 총 최대 28개
// 근데 올바른 괄호 조합의 개수를 구하는 문제

// 올바른 괄호 조합은
// 열림 괄호와 닫힘 괄호의 개수는 동일하다
// 열림괄호의 위치가 정해지면 닫힘괄호의 위치도 정해진다.
// 28C14 == 40116600으로 DP보다 느리겠지만 비벼볼만 하다.
// 쨌든 통과함

/**
 * 올바른 괄호 체크기
 */
class Check {
    static boolean check(char[] arr) {
        int stack = 0;

        for (char c : arr) {
            // 열림 괄호인 경우
            if (c == '(') {
                ++stack;
            }
            // 닫힘 괄호인 경우
            // 열림 괄호를 하나 빼야함
            else {
                if (stack == 0)
                    return false;
                --stack;
            }
        }

        if (stack == 0)
            return true;
        else
            return false;
    }
}

/**
 * n에 따른 조합을 만들고 올바른 괄호인지 체크한다
 */
class Arr {
    private char[] arr;
    private int n;
    private int ret;

    private void initArr(int n) {
        this.ret = 0;
        this.n = n;
        this.arr = new char[2 * n];
        Arrays.fill(this.arr, ')');
    }

    // cnt == 열림괄호를 채운 개수
    private void setCombiArr(int idx, int cnt) {
        if (cnt == n) {
            if (Check.check(arr)) {
                ++ret;
            }
        }

        for (int i = idx + 1; i < arr.length; ++i) {
            arr[i] = '('; // 열림 괄호
            setCombiArr(i, cnt + 1);
            arr[i] = ')';
        }

    }

    public int getRet(int n) {
        initArr(n);
        setCombiArr(-1, 0);
        return ret;
    }
}

class Solution {
    public int solution(int n) {
        return new Arr().getRet(n);
    }
}