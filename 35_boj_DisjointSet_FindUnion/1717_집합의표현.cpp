#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

#define MAX 1000000
int N, M;
int arr[MAX + 1] = { 0, };	// ������ �ʱ� [0, n]���� N+1���� ���Ұ� �ִٰ� ��
bool ran = true;

int found(int i) {
	// ������ ��ǥ idx(��Ʈ)�� ã�Ҵٸ�
	if (arr[i] == i) {
		return i;
	}
	// ����ȭ :: ��� ���� ����ȭ
	return arr[i] = found(arr[i]);
}

// union ����� ��� �Ұ���
void merge(int a, int b) {
	int a_root = found(a);
	int b_root = found(b);
	if ((a == b) || (a_root == b_root)) {	// ���� �׷��� ���
		return;
	}

	// �߸� ����ȭ :: merge�� ��ӵǴ� ��� ���� �� ����
	if (ran)
		arr[a_root] = b_root;
	else
		arr[b_root] = a_root;
	ran = !ran;

	return;
}

int main(int argc, char** argv) {

	cin >> N >> M;

	for (int i = 0; i <= N; ++i) {
		arr[i] = i;	// �ʱ� ����
	}


	for (int i = 0; i < M; ++i) {
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);	// cin -> scanf ���� �� �ð��ʰ� �ذ�;;
		// union
		if (a == 0) {
			merge(b, c);
		}// found
		else if (a == 1) {
			if ((b == c) || (found(b) == found(c))) {
				printf("YES\n");
			}
			else {
				printf("NO\n");
			}
		}// �̷� �Է��� ����
		else {
			cout << "ERROR" << endl;
		}
	}

	return 0;
}