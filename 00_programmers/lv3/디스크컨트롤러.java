import java.util.*;

class Solution {
    static class Job {
        int requestTime;
        int burstTime;

        public Job(int requestTime, int burstTime) {
            super();
            this.requestTime = requestTime;
            this.burstTime = burstTime;
        }

        @Override
        public String toString() {
            return "(" + requestTime + ", " + burstTime + ")";
        }

    }

    public int solution(int[][] jobs) {
        int answer = 0;

        Job[] jobArr = new Job[jobs.length];
        for (int i = 0; i < jobs.length; ++i) {
            jobArr[i] = new Job(jobs[i][0], jobs[i][1]);
        }

        Arrays.sort(jobArr, new Comparator<Job>(){
            // 요청이 먼저 들어온 순서대로 정렬한다.
            // 요청이 들어온 시간이 같다면 소요시간이 적은 순서대로 정렬한다.
            @Override
            public int compare(Job o1, Job o2) {
                if(o1.requestTime != o2.requestTime)
                    return o1.requestTime - o2.requestTime;
                else
                    return o1.burstTime - o2.burstTime;
            }
        });
        // System.out.println(Arrays.toString(jobArr));

        PriorityQueue<Job> pq = new PriorityQueue<>(new Comparator<Job>() {
            // cpu 사용량이 적은 작업이 우선순위를 갖는다
            // 같다면 요청시간이 빨랐던 작업이 우선순위를 갖는다.
            @Override
            public int compare(Job o1, Job o2) {
                if(o1.burstTime != o2.burstTime)
                    return o1.burstTime - o2.burstTime;
                else
                    return o1.requestTime - o2.requestTime;
            }
        });

        int idx = 0;
        int maxIdx = jobArr.length;

        int endTime = 0;
        int sumWaitTime = 0;

        while (!pq.isEmpty() || idx < maxIdx) {
            if (idx < maxIdx && jobArr[idx].requestTime <= endTime) {
                pq.add(jobArr[idx]);
                idx++;
                continue;
            }

            if (pq.isEmpty()) {
                sumWaitTime += jobArr[idx].burstTime;
                endTime = jobArr[idx].requestTime + jobArr[idx].burstTime;
                ++idx;
            } else {
                Job todo = pq.poll();
                sumWaitTime += (endTime - todo.requestTime) + todo.burstTime;
                endTime += todo.burstTime;
            }
        }

        answer = Math.floorDiv(sumWaitTime, maxIdx);
        System.out.println(answer);
        return answer;
    }
}