#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef struct _Node {
    int x;
    int y;
    int value;
}Node;
// x좌표값을 기준으로 오름차순 정렬하기
bool cmp(Node& n1, Node& n2) {
    return n1.x < n2.x;
}

vector<Node> arr;
// 전위 순회, M(루트)LR
void preorder(int left, int right, vector<int>& ret) {
    // [left, right]구간의 루트 위치를 찾는다
    int y_max = -1, root_idx = -1;
    for (int i = left; i <= right; ++i) {
        if (arr[i].y > y_max) {
            y_max = arr[i].y;
            root_idx = i;
        }
    }
    // root_idx를 찾지 못한 경우
    if (root_idx == -1)
        return;

    // 루트 방문
    ret.push_back(arr[root_idx].value);

    // 왼쪽 서브트리를 방문
    preorder(left, root_idx - 1, ret);

    // 오른쪽 서브트리를 방문
    preorder(root_idx + 1, right, ret);
}
// 후위 순회, LRM(루트)
void postorder(int left, int right, vector<int>& ret) {
    // [left, right]구간의 루트 위치를 찾는다
    int y_max = -1, root_idx = -1;
    for (int i = left; i <= right; ++i) {
        if (arr[i].y > y_max) {
            y_max = arr[i].y;
            root_idx = i;
        }
    }
    // root_idx를 찾지 못한 경우
    if (root_idx == -1)
        return;

    // 왼쪽 서브트리 방문
    postorder(left, root_idx - 1, ret);

    // 오른쪽 서브트리 방문
    postorder(root_idx + 1, right, ret);

    // 루트 방문
    ret.push_back(arr[root_idx].value);
}

vector<vector<int> > solution(vector<vector<int> > nodeinfo) {
    vector<vector<int> > answer;
    // 노드의 최대 개수는 10000개 이고, 그래프의 최대 깊이는 1000이므로
    // 배열이 아닌 link로 그래프를 표현하면 어떨까 생각했지만, 너무 복잡할것 같음
    // x축은 좌표는 곂치지 않는다 하였으므로, 모두 일직선에 위치시킬수 있을것 같다는 생각을 함
    // 어떤 트리의 최상위 노드는 구간에서 가장 큰 y값을 가지는 노드

    for (int i = 0; i < nodeinfo.size(); ++i) {
        int x = nodeinfo[i][0], y = nodeinfo[i][1], value = i + 1;
        arr.push_back({ x, y, value });
    }

    // x축에 평행하게 일직선에 위치시키기(x좌표 기준 정렬)
    sort(arr.begin(), arr.end(), cmp);
    /*for (int i = 0; i < arr.size(); ++i) {
        cout << arr[i].value << " ";
    }cout << endl;*/

    // 전위 순회
    vector<int> pre_ret;
    preorder(0, arr.size() - 1, pre_ret);
    /*for (int i = 0; i < pre_ret.size(); ++i) {
        cout << pre_ret[i] << " ";
    }cout << "\n";*/

    // 후위 순회
    vector<int> post_ret;
    postorder(0, arr.size() - 1, post_ret);
    /*for (int i = 0; i < pre_ret.size(); ++i) {
        cout << post_ret[i] << " ";
    }cout << "\n";*/

    answer = { pre_ret, post_ret };

    return answer;
}