import java.util.List;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int[] solution(int[] arr) {
        // 원소가 한개일 경우 -1 배열 반환
        if (arr.length == 1)
            return new int[] { -1 };

        // 반환 배열 크기는 받은 배열 크기 -1
        int[] answer = new int[arr.length - 1];
        
        // primitive 타입을 list로 변환(min 함수 사용하기 위해서)
        List<Integer> tmp = Arrays.stream(arr).boxed().collect(Collectors.toList());
        int min = Collections.min(tmp); // 최소값 구하기
        
        int answer_idx = 0;
        for (int num : tmp) {
            if (num!=min) {
                answer[answer_idx] = num;
                ++answer_idx;
            }
        }
        
        return answer;
    }
}