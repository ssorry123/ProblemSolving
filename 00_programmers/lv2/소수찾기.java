import java.util.*;

class Solution {
    boolean[] visited;
    Set<Integer> ret;

    void dfs(String numbers, String str, int lev) {
        // 소수인 경우 집합에 삽입
        if (str.length() > 0) {
            // string -> int
            int tmp = Integer.parseInt(str);
            if (check(tmp)) {
                ret.add(tmp);
            }
        }
        // 문자열의 길이만큼 소수를 만들어 봤다면
        if (lev == numbers.length())
            return;

        // 깊이 우선 탐색, 문자열을 붙여가며 만들어 본다
        for (int i = 0; i < numbers.length(); ++i) {
            if (!visited[i]) {
                String tmp = str;
                str += numbers.substring(i, i + 1);
                visited[i] = true;
                dfs(numbers, str, lev + 1);
                str = tmp;
                visited[i] = false;
            }
        }
    }

    // 소수 판별
    boolean check(int n) {
        if (n <= 1)
            return false;
        if (n == 2)
            return true;
        int nsqrt = (int) Math.sqrt(n);
        for (int i = 2; i <= nsqrt; ++i)
            if (n % i == 0)
                return false;
        return true;
    }

    public int solution(String numbers) {
        visited = new boolean[numbers.length()];
        Arrays.fill(visited, false);

        ret = new HashSet<>();

        dfs(numbers, "", 0);

        return ret.size();
    }
}
