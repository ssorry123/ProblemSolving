#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool comp(int& s1, int& s2) {
	int s1_len = to_string(s1).length();
	int s2_len = to_string(s2).length();
	int s1s2 = s1 * pow(10, s2_len) + s2;
	int s2s1 = s2 * pow(10, s1_len) + s1;
	// s1s2가 더 크면 왼쪽(먼저 정렬되어야)에 위치해야 함
	return s1s2 > s2s1;
}

string solution(vector<int> numbers) {
	string answer = "";
	sort(numbers.begin(), numbers.end(), comp);
	// 0이 맨 왼쪽에 오면 안됨
	int k = 0;
	while (k < numbers.size() && numbers[k] == 0)
		++k;
	// 모든 숫자가 0인 경우
	if (k == numbers.size())
		answer = "0";
	for (int i = k; i < numbers.size(); ++i)
		answer += to_string(numbers[i]);

	return answer;
}