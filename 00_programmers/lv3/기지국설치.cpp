#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

/*
기지국을 설치하면, 양쪽으로 w만큼 퍼져나간다
즉 본인포함해서 양쪽 w, ==> 2*w+1만큼 전파가 전달됨
station은 이미 설치되어 있는 기지국을 알려줌
아파트 번호는 1번부터 시작함
*/
// n은 최대 2억이므로 배열을 만들기는 힘들거같다
int solution(int n, vector<int> stations, int w)
{
    int answer = 0;

    const int ONE_COVER_RANGE = 2 * w + 1;  // 한 기지국이 커버하는 범위
    int last_cover = 0; // 0~last_cover까지 기지국이 커버 중

    for (int i = 0; i < stations.size(); ++i) {
        int at = stations[i];
        int left = at - w, right = at + w;
        if (left <= 0)
            left = 1;
        if (right > n)
            right = n;

        int no_cover_cnt = left - last_cover - 1;
        // left의 앞부분들이 모두 커버 중이라면
        if (no_cover_cnt <= 0) {
            last_cover = right;
            continue;
        }
        
        int need = ceil((double)no_cover_cnt / ONE_COVER_RANGE);
        answer += need;
        last_cover = right;
    }

    // 커버 안된 구간 처리
    if (last_cover < n)
        answer += ceil(double(n - last_cover) / ONE_COVER_RANGE);


    return answer;
}