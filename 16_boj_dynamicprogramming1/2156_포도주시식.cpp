#include<iostream>
#include<algorithm>

using namespace std;

#define MAX 10001

int N;
int S[MAX];
int p[MAX];

int main() {
	cin >> N;
	for (int i = 1; i <= N; ++i) {
		cin >> p[i];
	}

	S[0] = 0;
	S[1] = p[1];
	S[2] = p[1] + p[2];

	/*
	i-2   i-1    i
	 X     O     O
	 O     X     O
	 O     O     X
	*/

	for (int i = 3; i <= N; ++i) {
		int a, b, c;
		a = S[i - 3] + p[i-1] + p[i];
		b = S[i - 2] + p[i];
		c = S[i - 1];
		int tmp = max(a, b);
		tmp = max(tmp, c);
		// cout << tmp << endl;
		S[i] = tmp;
	}

	cout << S[N] << endl;

	return 0;
}