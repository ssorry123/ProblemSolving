#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
typedef struct _idxfail {
    int idx;
    double fail;
}F;
// c++ pq 우선순위는 값이 작은 것?
struct cmp {
    bool operator() (F& f1, F& f2) {
        // 새로 들어온 f2 fail의 값이 크면 우선순위가 높다
        if (f1.fail != f2.fail)
            return f1.fail < f2.fail;
        // 새로 들어온 f2 idx가 작으면 우선순위가 높다
        else {
            cout << "operator" << endl;
            return f1.idx > f2.idx;
        }
    }
};

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;

    // [1] ~ [N+1] 사용
    vector<int> tmp(N + 2, 0);
    vector<int> tmp_sum(N + 2, 0);  // 1<=<=i 까지 tmp의 합
    for (int i = 0; i < stages.size(); ++i)
        ++tmp[stages[i]];
    for (int i = 1; i < N + 2; ++i)
        tmp_sum[i] = tmp_sum[i - 1] + tmp[i];

    // [1] ~ [N] 사용
    priority_queue< F, vector<F>, cmp> pq;
    // i stage의 실패율 계산
    // (1) i ~ N+1 stage 사람 수 합 -> i stage에 도달한 사람
    // (2) i stage 사람수 -> i stage에 도달했으나 아직 클리어하지 않음
    // fail = (2) / (1)
    for (int i = 1; i <= N; ++i) {
        // 해당 스테이지를 도달 했으나 클리어 하지 못한 사람수(분자)가 0이 아닌 경우
        // 해당 스테이지에 도달한 사람수(분모)는 0이 될 수 없다.

        // (분자)가 0인 경우, (분모)는 0일 수도 있고, 아닐 수도 있다.
        // (해당 스테이지까지 아무도 도달하지 못한 경우, 더 높은 스테이지를 깨고 있는 경우)

        // (분자)가 0인 경우 항상 실패율은 0이므로 따로 처리를 해줘야함
        // 0으로 나누게 되는 경우, 값은 INF가 된다
        if (tmp[i] == 0) {
            pq.push({ i, 0 });
            continue;
        }
        double fail = double(tmp[i]) / (tmp_sum[N + 1] - tmp_sum[i - 1]);
        pq.push({ i, fail });
    }

    while (!pq.empty()) {
        cout << pq.top().idx << " " << pq.top().fail << endl;
        answer.push_back(pq.top().idx);
        pq.pop();
    }

    return answer;
}
