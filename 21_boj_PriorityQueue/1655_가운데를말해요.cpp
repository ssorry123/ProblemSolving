#include <queue>
#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

// 중간값을 말해요
// 중간 값 heap을 설계해야 함
// 중간 값 heap === maxHeap 연결 minHeap
/*
- 중간 값은, left힙에 위치하도록 설계한다
-> 즉 size(leftH) == size(rightH)+1 or same
- right힙의 원소들은 mid값보다 크거나 같은 값들로 이루어져 있을 것
- left힙의 원소들은  mid값보다 작거나 같은 값들로 이루어져 있을 것
*/
priority_queue<int, vector<int>, less<int> > leftHeap;      // maxHeap
priority_queue<int, vector<int>, greater<int> > rightHeap;  // minHeap
int cnt = 0;
// 삽입만 한다, 삭제할 일은 없다
int insert(int val) {
    // 비어있는, 중간값 힙에 삽입
    if (cnt == 0) {
        leftHeap.push(val);
        ++cnt;
        return 0;
    }

    int leftSize = leftHeap.size();
    int rightSize = rightHeap.size();
    // 왼쪽 힙과, 오른쪽 힙의 크기가 같을때
    if (leftSize == rightSize) {
        int mid = leftHeap.top();
        // [,,, mid(max)] [min ,,,]
        if (val > mid) {
            // val은 right힙에 들어가게 되고, min(right힙)이 중간값이 된다
            rightHeap.push(val);
            int new_mid = rightHeap.top();
            rightHeap.pop();		// 중간값 right에서 제거
            leftHeap.push(new_mid);	// 중간값 left에 추가
        }
        else {
            leftHeap.push(val);
        }
        ++cnt;
        return 0;
    }
    // (왼쪽 힙과, 오른쪽 힙의 크기가 다를때)
    else if (leftSize == rightSize+1) {
        int mid = leftHeap.top();
        if (val >= mid) {
            rightHeap.push(val);	// 중간값은 변하지 않는다
        }
        else {
            rightHeap.push(mid);	// mid를 옮김
            leftHeap.pop();			// mid를 제거
            leftHeap.push(val);		// 새로운 값 추가
        }
        ++cnt;
        return 0;
    }
    // 그 외의 상황은 존재하지 않도록 설계
    else {
        printf("ERROR\n");
        return -1;
    }
}
int search() {
    return leftHeap.top();
}
int main() {
    int N;
    scanf("%d", &N);

    for (int i = 1; i <= N; ++i) {   // O(n)
        // 수빈이가 말한 값 삽입
        int subin;
        scanf("%d", &subin);
        
        if (insert(subin) == -1)	// 삽입 에러 검사
            break;

        printf("%d\n", search());
    }

    return 0;
}
