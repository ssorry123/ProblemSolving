#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

typedef vector<vector<int> > vvi;
vector<int> sccID;
vector<int> discoverd;
stack<int> st;
int sccCnt, vCnt;

int scc(int here, vvi& arr) {
    // here은 몇번째로 발견되었는가?
    int ret = discoverd[here] = vCnt++;
    // here이후에 발견되는 v들은 here과 같은 scc에 포함될 가능성이 있다
    st.push(here);

    // here과 연결된 v들을 검사
    for (int i = 0; i < arr[here].size(); ++i) {
        int there = arr[here][i];

        // 방문하지 않은경우 방문한다
        // there을 루트로하는 서브트리에서 here의 선조에 방문하지 않는다면
        // ret은 변하지 않는다
        if (discoverd[there] == -1) {
            // tree edge
            ret = min(ret, scc(there, arr));
        }

        /*
        // there이 here보다 늦게 방문된 경우, 역방향 간선이 아닌 순방향 간선
        else if (discoverd[here] < discoverd[there]) {
            // forword edge
        }
        
        else if (finished[there]==false)
            역방향 간선(싸이클이 존재)
        // there부터 dfs가 끝나지 않았는데, there을 방문하는 경우 싸이클이다
        // 역방향 간선이다 back edge
        */

        // 무시해야하는 교차간선으로 there을 가는 경우가 아니라면
        // (there의 sccID가 아직 정해지지 않았다면)
        else if (sccID[there] == -1) {
            // cross edge
            ret = min(ret, discoverd[there]);
            // there의 scc가 정해지지 않았는데, here보다 늦게 발견되었다면
            // here-there edge는 scc를 DAG로 바꿨을때 edge가 된다
        }
    }

    if (ret == discoverd[here]) {
        // scc 번호 결정
        while (true) {
            int t = st.top();
            st.pop();
            sccID[t] = sccCnt;
            if (t == here)
                break;
        }
        ++sccCnt;
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int V, E;
    cin >> V >> E;
    // 노드간 연결 저장
    vvi arr(V + 1, vector<int>());
    int a, b;
    for (int i = 0; i < E; ++i) {
        cin >> a >> b;
        arr[a].push_back(b);
    }

    // 각 v에 대해서 scc id 저장
    sccID = vector<int>(V + 1, -1);
    // v가 몇번째로 발견되었는지 저장
    discoverd = vector<int>(V + 1, -1);
    sccCnt = vCnt = 0;

    // 모든 노드에대해서, scc 검사
    for (int i = 1; i <= V; ++i) {
        if (discoverd[i] == -1)
            scc(i, arr);
    }

    // 정답 출력
    cout << sccCnt << "\n";
    discoverd = vector<int>(V + 1, -1);
    for (int i = 1; i <= V; ++i) {
        if (discoverd[i] == -1) {
            discoverd[i] = 0;
            int tmp = sccID[i];
            for (int j = i; j <= V; ++j) {
                if (sccID[j] == tmp) {
                    cout << j << " ";
                    discoverd[j] = 0;
                }
            }
            cout << -1 << "\n";
        }
    }

    return 0;
}