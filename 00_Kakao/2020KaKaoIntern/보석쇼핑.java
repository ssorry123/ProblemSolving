import java.util.*;

class Ret {
    Integer start;
    Integer end;
    Integer size;

    Ret(int start, int end) {
        this.start = start;
        this.end = end;
        this.size = end - start + 1;
    }
}

class RetCmp implements Comparator<Ret> {

    @Override
    public int compare(Ret o1, Ret o2) {
        // TODO Auto-generated method stub
        // 범위가 다르다면, 범위가 짧은 것 우선
        if (o1.size != o2.size) {
            return o1.size.compareTo(o2.size);
        }
        // 범위가 같다면, 먼저 있는 것
        else {
            return o1.start.compareTo(o2.start);
        }

    }

}

class Solution {

    HashMap<String, Integer> hm;

    public void hmAdd(String key) {
        // 이미 있는 보석이라면, 갯수 추가
        if (hm.containsKey(key)) {
            hm.replace(key, hm.get(key) + 1);
        }
        // 처음 사는 보석이라면, 새로운 키 추가
        else {
            hm.put(key, 1);
        }
    }

    public void hmDel(String key) {
        // 없는 보석을 삭제하는 경우 오류
        if (!hm.containsKey(key))
            System.exit(1);

        // 보석 개수 1개 감소
        hm.replace(key, hm.get(key) - 1);
        // 0개가 되면 삭제
        if (hm.get(key) == 0) {
            hm.remove(key);
        }
    }

    public int hmSize() {
        return hm.size();
    }

    // 전체 보석의 수를 구하는 함수
    public int getGemCount(String[] gems, int start, int end) {
        Set<String> set = new HashSet<>();
        for (int i = start; i <= end; ++i) {
            // 포함하지 않는다면
            String gem = gems[i];
            if (!set.contains(gem)) {
                set.add(gem);
            }
        }
        return set.size();
    }

    public int[] solution(String[] gems) {

        // 전체 보석의 종류 개수를 구한다.
        int gemCount = getGemCount(gems, 0, gems.length - 1);
        System.out.println("보석 개수 : " + gemCount);

        // 투 포인터
        int start = 0; // 구입한 보석 범위 시작 위치
        int end = 0; // 다음에 구입할 보석 위치
        // start가 end 왼쪽에 있고,
        // end를 더 늘릴 수 있다면
        List<Ret> list = new ArrayList<>();
        hm = new HashMap<>();

        while (true) {
            // 모든 종류 보석을 구매하였다면
            if (hmSize() == gemCount) {
                list.add(new Ret(start, end - 1)); // 기록
                hmDel(gems[start]); // start 제거하고(범위를 좁히고)
                start++; // start 이동
            }
            // 모든 종류 보석을 구매하지 못했다면
            // 새로운 보석을 구입한다
            else {
                hmAdd(gems[end++]);
            }

            // 더이상 보석을 구매할 수 없고
            // 현재 범위로 모든 종류 보석을 구매하지 못했다면
            // start를 늘리는 것은 의미 없음(범위를 좁히는 것은 의미 없음)
            // (모든 보석을 구매한 경우 한번 더 루프를 돌고 기록 후 탈출)
            if (end >= gems.length && hmSize() < gemCount) {
                break;
            }

        }

        int[] answer = { 0, 0 };
        Collections.sort(list, new RetCmp()); // 특수한 기준으로 정렬
        Ret ret = list.get(0); // 반드시 가능한 정답이 존재
        // 인덱스는 1부터 시작
        answer[0] = ret.start + 1;
        answer[1] = ret.end + 1;

        System.out.println(Arrays.toString(answer));

        return answer;
    }

}