import java.util.*;

// 두 아들은 같은 양의 과자를 받아야 한다.

class Solution {

    public int solution(int[] cookie) {
        int answer = 0;

        // ( ? ... m) (m+1 ... ?)
        for (int m = 0; m < cookie.length - 1; ++m) {
            int lIdx = m;
            int rIdx = m + 1;
            int lSon = cookie[lIdx];
            int rSon = cookie[rIdx];

            while (true) {
                // 왼쪽 아들이 더 적게 받은 경우
                if (lSon < rSon) {
                    if (lIdx - 1 >= 0)
                        lSon += cookie[--lIdx];
                    else
                        break; // 더 늘릴 수 없는 경우
                }
                // 오른쪽 아들이 더 적게 받은 경우
                else if (lSon > rSon) {
                    if (rIdx + 1 < cookie.length)
                        rSon += cookie[++rIdx];
                    else
                        break;
                }
                // 둘이 같은 경우
                else {
                    answer = Math.max(answer, rSon);
                    // 더 큰 정답이 있을 수 있으므로 찾아 떠난다.
                    if (lIdx - 1 >= 0 && rIdx + 1 < cookie.length) {
                        lSon += cookie[--lIdx];
                        rSon += cookie[++rIdx];
                    }
                    // 확장 불가이므로 멈춘다.
                    else {
                        break;
                    }
                }
            }
        }

        return answer;
    }
}