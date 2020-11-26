class Solution {
    public boolean solution(int x) {

        // 자리수 합을 구하기위해 int -> String
        String str = Integer.toString(x);

        int sum = 0;
        for (int i = 0; i < str.length(); ++i) {
            // parseInt( String, int)
            sum += Integer.parseInt(String.valueOf(str.charAt(i)), 10);
        }

        // System.out.println(sum);

        // 하샤드 수
        if (x % sum == 0)
            return true;
        return false;
    }
}