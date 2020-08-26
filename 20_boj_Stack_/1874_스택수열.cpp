#include<cstdio>
#include<stack>
#include<vector>

using std::stack; using std::vector;

int main(int argc, char** argv) {
	int N;
	stack<int> s;
	vector<int> v;		// ���� ����
	vector<char> ret;	// ���� ����

	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		int tmp;
		scanf("%d", &tmp);
		v.push_back(tmp);
	}

	// ���ÿ� �����͵��� ������ ������ ������� ������ ����� ����
	int push_val = 1;
	int arr_idx = 0;
	// �� ���� ���� �ְų� �� ���� �ִٸ�
	while (!s.empty() || push_val <= N) {
		// �ѹ��� ���ۿ� �ְų�, ���ų�

		// top�� ���� �������ϴ� �����
		// (arr_idx�� �ε����� ��� ���� ����)
		if (!s.empty() && s.top() == v[arr_idx]) {
			// printf("%d ", s.top());
			s.pop();	// ����
			++arr_idx;	// �������ϴ� ���� �迭 �ε���
			ret.push_back('-');
		}
		// �� ���� ���� ���µ� �� �� �ִ� �͵� ���� ��(������ �ð� �ʰ�)
		else if ((push_val > N) && (s.empty() || s.top() != v[arr_idx])) {
			break;
		}
		else {
			// ���� ���� �� ������
			if (push_val <= N) {
				s.push(push_val++);
				ret.push_back('+');
			}
		}
	}

	// N���� ������ ��� ������ٸ�
	if (arr_idx != N)
		printf("NO");
	else {
		for (int i = 0; i < ret.size(); ++i)
			printf("%c\n", ret[i]);
	}

	return 0;
}
