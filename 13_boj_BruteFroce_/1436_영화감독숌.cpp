#include<iostream>

using namespace std;

// 3자리 = 666
// 4자리 = x666, 666x
// 5자리 = xx666, x666x, 666xx

typedef unsigned int uint;

// 6이 연속으로 3번 존재하는지 검사
int check(uint i) {
	int ret = 0;
	
	int cnt = 0;
	while (i != 0) {
		// 가장 오른쪽 숫자가 6
		if (i % 10 == 6)
			++cnt;
		else
			cnt = 0;
		
		// 연속으로 6이 3번 나온 경우
		if (cnt == 3)
			return 1;

		// 다음 수 검사
		i /= 10;
	}
	return 0;
}

int main(int argc, char** argv) {
	int N;
	cin >> N;
	int cnt = 0;
	unsigned int i = 666;
	while (cnt < N) {
		if (check(i))
			++cnt;
		++i;
	}
	cout << i - 1;

	return 0;
}

