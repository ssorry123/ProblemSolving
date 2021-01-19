import java.util.Arrays;
import java.util.HashMap;

class Solution {
    HashMap<String, Integer> ctoi;
    int[] arr; // 각 사람들이 앉을 위치
    String[] idata;
    boolean[] visited; // 각 사람들이 자리에 앉았는지 확인

    public int getIndexOfArr(char c) {
        String tmp = String.valueOf(c);
        int val = ctoi.get(tmp);
        for (int i = 0; i < arr.length; ++i) {
            if (arr[i] == val) {
                return i;
            }
        }
        return -1;
    }

    public int dfs(int idx) {
        // 8명의 자리를 다 정하였다면, 조건을 확인한다
        if (idx == arr.length) {
            for (int i = 0; i < idata.length; ++i) {
                String tmp = idata[i];

                int aPerson = getIndexOfArr(tmp.charAt(0));
                int bPerson = getIndexOfArr(tmp.charAt(2));
                char op = tmp.charAt(3);
                int abDist = Math.abs(aPerson - bPerson) - 1;
                int dist = Integer.valueOf(String.valueOf(tmp.charAt(4)));

                if (op == '=' && abDist != dist)
                    return 0;
                if (op == '>' && abDist <= dist)
                    return 0;
                if (op == '<' && abDist >= dist)
                    return 0;
            }

            return 1;
        }

        int ret = 0;

        // 8명의 자리를 정하기 전, idx 자리에 앉을 사람을 정한다
        for (int i = 0; i < visited.length; ++i) {
            // i라는 사람이 아직 자리가 정해지지 않았다면
            if (!visited[i]) {
                visited[i] = true; // 자리 정함
                arr[idx] = i; // 실제로 자리에 앉힘
                ret += dfs(idx + 1); // 다음 자리의 사람을 정하러 감
                visited[i] = false;
            }
        }

        return ret;
    }

    public int solution(int n, String[] data) {
        idata = data;
        // 8명이므로, 가능한 자리 조합은 8! == 40320 개이다
        // 모든 조합을 만들어보고, 조건에 맞는지 확인해도 될듯

        // 캐릭터 이름들을, 숫자로 매칭시킨다
        ctoi = new HashMap<>();
        String[] name = { "A", "C", "F", "J", "M", "N", "R", "T" };
        for (int i = 0; i < name.length; ++i) {
            ctoi.put(name[i], i);
        }

        // 변수 초기화
        arr = new int[name.length];
        visited = new boolean[name.length];
        Arrays.fill(visited, false);

        return dfs(0);
    }
}