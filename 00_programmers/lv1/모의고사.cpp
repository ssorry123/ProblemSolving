#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> answers) {
	vector<int> answer;
	vector<vector<int> > supoza = {
		{1, 2, 3, 4, 5},
		{2,1,2,3,2,4,2,5},
		{3,3,1,1,2,2,4,4,5,5}
	};
	vector<int> sum = { 0, 0, 0 };
	// 0번~2번사람까지 몇문제 맞췄는지 세기
	for (int i = 0; i < 3; ++i) {
		int k = 0;
		for (int j = 0; j < answers.size(); ++j) {
			if (supoza[i][k] == answers[j])
				++sum[i];
			k = (k + 1) % supoza[i].size();
		}
	}
	// 0번~2번중 맞춘 문제수 최대값 구하기
	int max = -1;
	for (int i = 0; i < 3; ++i) {
		int id = -1;
		if (sum[i] > max)
			max = sum[i];
	}
	// 최대값에 해당하는 사람들 결과에 넣기
	for (int i = 0; i < 3; ++i) {
		if (sum[i] == max)
			answer.push_back(i + 1);
	}

	return answer;
}