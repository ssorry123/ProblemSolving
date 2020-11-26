class Solution {

    public static int manhattanDis(int finger, int target) {
        int[] fLoc = { 0, 0 };
        int[] tLoc = { 0, 0 };

        // set finger Location
        if (finger == -1) {
            fLoc = new int[] { 3, 0 };
        } else if (finger == -2) {
            fLoc = new int[] { 3, 2 };
        } else if (finger == 0) {
            fLoc = new int[] { 3, 1 };
        } else {
            fLoc[0] = (finger - 1) / 3;
            fLoc[1] = (finger - 1) % 3;
        }

        // set target Location
        if (target == 0) {
            tLoc = new int[] { 3, 1 };
        } else {
            tLoc[0] = (target - 1) / 3;
            tLoc[1] = (target - 1) % 3;
        }

        return Math.abs(fLoc[0] - tLoc[0]) + Math.abs(fLoc[1] - tLoc[1]);
    }

    public String solution(int[] numbers, String hand) {
        String answer = "";

        int left = -1; // 왼손 초기 위치 *
        int right = -2; // 오른손 초기 위치 #

        for (int num : numbers) {
            // use left
            if (num == 1 || num == 4 || num == 7) {
                answer += "L";
                left = num;
            }
            // use right
            else if (num == 3 || num == 6 || num == 9) {
                answer += "R";
                right = num;
            }
            // use near (middle)
            else {
                int leftDis = Solution.manhattanDis(left, num);
                int rightDis = Solution.manhattanDis(right, num);

                // 가까운 손가락으로 사용
                if (leftDis < rightDis) {
                    answer += "L";
                    left = num;
                } else if (rightDis < leftDis) {
                    answer += "R";
                    right = num;
                    // 거리가 같으면 어느 손을 사용하는지 보고 결정
                } else {
                    if (hand.equals("left")) {
                        answer += "L";
                        left = num;
                    } else {
                        answer += "R";
                        right = num;
                    }
                }
            }
        }

        return answer;
    }
}
