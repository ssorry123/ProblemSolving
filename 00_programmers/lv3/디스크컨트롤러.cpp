// waiting time을 가장 적게 만드는
// Shortest Job First Scheduling

#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

typedef struct _job {
    int request_time;
    int burst_time;
}job;

// 우선순위큐 정렬
struct job_comp {
    // cpu 사용량이 적은 작업이 우선순위를 갖는다
    // cpu 사용량이 같다면 요청 시간이 빨랐던 작업이 우선순위를 갖는다.
    bool operator()(job& a, job& b) {
        if (a.burst_time != b.burst_time)
            return a.burst_time > b.burst_time;
        else
            return a.request_time > b.request_time;
    }
};
priority_queue<job, vector<job>, job_comp> pq;

// 초기 벡터 정렬 용
bool jobs_comp(vector<int>& a, vector<int>& b) {
    // 요청이 들어온 시간이 빠른 순으로 정렬한다
    if (a[0] != b[0])
        return a[0] < b[0];
    // 요청이 들어온 시간이 같다면, cpu 사용량이 적은 순서대로 정렬한다
    else
        return a[1] < b[1];
}

int solution(vector<vector<int>> jobs) {
    int answer = 0;

    sort(jobs.begin(), jobs.end(), jobs_comp);  // 시간 순 대로 정렬

    int idx = 0;
    const int max_idx = jobs.size();

    int end_time = 0;
    int sum_wait_time = 0;

    // 대기큐에 남아있는 작업이 있거나, 아직 시간이 되지 않아서 작업이 들어오지 않은 경우
    while (!pq.empty() || idx < max_idx) {
        // 작업이 끝나고 새로운 작업을 시작할 수 있게 되었을 때
        // 그 전에 들어온 요청이 있었다면 대기 큐에 추가
        if (idx < max_idx && jobs[idx][0] <= end_time) {
            pq.push({ jobs[idx][0], jobs[idx][1] });
            idx++;
            continue;
        }


        // 대기 중인 작업이 없을 경우, 가장 빠른 작업을 수행
        if (pq.empty()) {
            sum_wait_time += jobs[idx][1];          // 기다린 시간 기록
            end_time = jobs[idx][0] + jobs[idx][1]; // 작업을 끝낸 후 시간 기록
            ++idx;
        }
        // 대기 중인 작업이 있을 경우, 우선순위에 따라 작업을 수행
        else {
            job todo = pq.top(); pq.pop();
            sum_wait_time += (end_time - todo.request_time) + todo.burst_time;
            end_time += todo.burst_time;
        }
    };

    std::cout << "sum time :: " << sum_wait_time << endl;
    answer = (int)floor(sum_wait_time / max_idx);



    return answer;
}

int main() {

    solution({ {0,3}, {1,9}, {2,6} });
    return 0;
}