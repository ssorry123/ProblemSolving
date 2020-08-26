#include<iostream>

using namespace std;

// 3�ڸ� = 666
// 4�ڸ� = x666, 666x
// 5�ڸ� = xx666, x666x, 666xx

typedef unsigned int uint;

// 6�� �������� 3�� �����ϴ��� �˻�
int check(uint i) {
	int ret = 0;
	
	int cnt = 0;
	while (i != 0) {
		// ���� ������ ���ڰ� 6
		if (i % 10 == 6)
			++cnt;
		else
			cnt = 0;
		
		// �������� 6�� 3�� ���� ���
		if (cnt == 3)
			return 1;

		// ���� �� �˻�
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

