#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;
	// 빌려줄 수 있는 학생들이 빌려주기만 한다면 최대 인원 수업 가능

	// 초기 학생들의 체육복 수
	vector<int> student(n + 1, 1);
	// 여벌 가져온 사람들
	for (int i = 0; i < reserve.size(); ++i)
		++student[reserve[i]];
	// 도둑 당한 학생들
	for (int i = 0; i < lost.size(); ++i)
		--student[lost[i]];
	// 체육복 수가 2인 학생들이 자신의 앞뒤번호에 0인 학생에게 체육복을 준다
	// 체육복을 줄 수 있는 학생이 처음 나타났을때 
	// 앞번호가 없다면 앞번호 먼저주고, 앞번호가 있을때에만 뒷번호에게 준다
	// 뒷번호에게 안주더라도 이후에 뒷번호는 뒷번호의뒷번호에게 받을 가능성이 있기 때문
	for (int i = 1; i <= n; ++i) {
		// 줄 수 있는 학생이라면
		if (student[i] == 2) {
			// 앞에 학생이 체육복이 없다면
			if (i - 1 > 0 && student[i - 1] == 0)
				student[i - 1] = student[i] = 1;
			// 앞번호는 있는데 뒷번호가 없다면
			else if (i + 1 <= n && student[i + 1] == 0)
				student[i] = student[i + 1] = 1;
			else {
				// 안 줌
			}
		}
	}
	// 체육복의 수가 1이상인 학생들의 수를 센다
	answer = 0;
	for (int i = 1; i <= n; ++i)
		if (student[i] >= 1)
			++answer;

	return answer;
}