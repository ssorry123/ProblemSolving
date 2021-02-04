import java.util.*;

class Solution {
	public int solution(int[] scoville, int K) {
		int answer = 0;

		PriorityQueue<Integer> pq = new PriorityQueue<Integer>(new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				// TODO Auto-generated method stub
				return o1 - o2;
			}
		});

		for (int t : scoville)
			pq.add(t);

		while (pq.peek() < K) {
			if (pq.size() == 1) {
				answer = -1;
				break;
			}
			int a = pq.poll();
			int b = pq.poll();

			pq.add(a + 2 * b);
			++answer;
		}

		return answer;
	}
}
