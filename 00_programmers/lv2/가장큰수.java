import java.util.*;

// 두 아들은 같은 양의 과자를 받아야 한다.

class Solution {
    public String solution(int[] numbers) {
        String answer = "";

        Integer[] nums = new Integer[numbers.length];
        for (int i = 0; i < numbers.length; ++i) {
            nums[i] = numbers[i];
        }

        Comparator<Integer> comp = new Comparator<>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int s1_len = o1.toString().length();
                int s2_len = o2.toString().length();
                int s1s2 = (int) (o1 * Math.pow(10, s2_len) + o2);
                int s2s1 = (int) (o2 * Math.pow(10, s1_len) + o1);
                return s2s1 - s1s2;
            }
        };

        Arrays.sort(nums, comp);
        
        int k = 0;
        while(k < nums.length && nums[k] == 0)
            ++k;
        
        if(k == nums.length)
            answer = "0";
        
        for(int i = k; i < nums.length; ++i)
            answer += nums[i].toString();

        return answer;
    }
}