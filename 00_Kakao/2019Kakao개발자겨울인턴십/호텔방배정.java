import java.util.*;

class Solution {

    // 자기 자신의 부모를 알려줌
    // 연속된 호텔방들은 하나의 집합에 속해있어야함
    // 하나의 집합의 루트는 연속된 호텔의 방 번호중 가장 큰 값임
    Map<Long, Long> res;

    long findRoot(long me) {
        // 내가 최고 조상이라면
        if (res.get(me) == me) {
            return me;
        }
        // 내가 최고 조상이 아니라면
        // 나의 부모를 조사해보자
        long ret = findRoot(res.get(me));
        res.replace(me, ret); // 경로 압축 최적화
        return ret;
    }

    // 두 집합을 합친다.
    // 핵심 :!! !! 두 집합 중 최고 조상이 더 큰 집합을 루트로 한다
    void union(long a, long b) {
        long aRoot = findRoot(a);
        long bRoot = findRoot(b);

        if (aRoot == bRoot)
            return;

        // aRoot가 더 크게 설정하자
        if (aRoot < bRoot) {
            long tmp = aRoot;
            aRoot = bRoot;
            bRoot = tmp;
        }

        // 두 집합중 더 큰 Root가 합쳐진 집합의 Root가 됨
        res.replace(bRoot, aRoot);
    }

    long nextRoom(long room) {
        // 최고 조상은 집합에서 가장 큰 값이다.
        // 최고조상보다 1큰 방을 배정해야 한다.
        // 최고조상보다 1큰 방도 배정되어있을 수도있다.
        // 그런 경우 두 집합을 합치고 다시 찾아야함
        long ret = findRoot(room) + 1;

        // 최고 조상보다 1큰 방도 배정되어 있다면
        // 배정되지 않은 방이 나올때까지 찾는다.
        while (res.containsKey(ret)) {
            union(ret, ret - 1); // 일단 인접한 두 집합을 합친다.
            ret = findRoot(ret) + 1; // 합쳐진 집합에서 다음 방을 찾는다.
        }
        return ret;
    }

    public long[] solution(long k, long[] room_number) {
        long[] answer = new long[room_number.length];
        int answerIdx = 0;

        // k는 long이므로 long크기의 배열을 만드는 것은 불가능하다
        // 배열이 아닌 dict으로 상호배타조합을 구현한다.
        res = new HashMap<>();

        for (long room : room_number) {
            // 해당 방번호가 아직 배정되지 않은 상태라면, 바로 배정
            if (!res.containsKey(room)) {
                res.put(room, room);
                answer[answerIdx++] = room;
                continue;
            }
            // 이미 배정된 방이라면 다른 방을 선택하야 함
            long nextRoom = nextRoom(room);
            // 정답을 추가한다.
            answer[answerIdx++] = nextRoom;
            // 새로운 방을 배정하고
            // 하나의 집합으로 합쳐야 한다.
            res.put(nextRoom, nextRoom);
            union(nextRoom, nextRoom);

        }

        // System.out.println(Arrays.toString(answer));

        return answer;
    }
}