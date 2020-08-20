#include<iostream>

using namespace std;

#define N 10

// LBS를 반환한다
bool get(int *num, int idx = 0) {
	return ((1 << idx) & *num) != 0;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		int ret = 0;
		int tmp = 0;
		for (int i = 0; i < N; ++i) {
			cin >> tmp;
			if (get(&tmp)) {
				ret += tmp;
			}
		}
		cout << "#" << test_case << " " << ret << "\n";
	}


	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}