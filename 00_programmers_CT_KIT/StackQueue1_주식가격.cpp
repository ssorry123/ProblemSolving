#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    for (int i = 0; i < prices.size(); ++i) {
        int cnt = 0;
        for (int j = i + 1; j < prices.size(); ++j)
            // 떨어지지 않았으면
            if (prices[i] <= prices[j])
                ++cnt;
            // 가격이 떨어졌으면
            else {
                ++cnt;
                break;
            }
        answer.push_back(cnt);
    }

    return answer;
}