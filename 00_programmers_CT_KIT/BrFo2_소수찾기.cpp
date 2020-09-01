#include <string>
#include <vector>
#include <set>
#include <cstdlib>
#include <cmath>
#include <iostream>

using namespace std;
// 소수 판별
bool check(int& n) {
	if (n <= 1)
		return false;
	if (n == 2)
		return true;
	int nsqrt = sqrt(n);
	for (int i = 2; i <= nsqrt; ++i)
		if (n % i == 0)
			return false;
	return true;
}
vector<bool> visited;
set<int> ret;
// dfs, 완전탐색
void dfs(string& numbers, string str = "", int lev = 0) {
	cout << str << endl;
	// 소수인 경우 집합에 삽입
	if (str.length() > 0) {
		// string -> int
		int tmp = atoi(str.c_str());
		if (check(tmp)) {
			ret.insert(tmp);
			// cout << tmp << endl;
		}
	}
	// 문자열의 길이만큼 소수를 만들어 봤다면
	if (lev == numbers.size())
		return;

	// 깊이 우선 탐색, 문자열을 붙여가며 만들어 본다
	for (int i = 0; i < numbers.size(); ++i) {
		if (!visited[i]) {
			string tmp = str;
			str += numbers.substr(i, 1);
			visited[i] = true;
			dfs(numbers, str, lev + 1);
			str = tmp;
			visited[i] = false;
		}
	}

}
int solution(string numbers) {
	int answer = 0;
	// 방문하였는지 여부
	visited.assign(numbers.length(), false);
	dfs(numbers);
	// 집합의 크기가 정답
	answer = ret.size();

	return answer;
}