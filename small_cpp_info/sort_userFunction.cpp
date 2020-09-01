#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

typedef struct Token {
	int a, b, c;
}Token;
void print(vector<Token>& v) {
	for (int i = 0; i < v.size(); ++i) {
		printf("%d %d %d\n", v[i].a, v[i].b, v[i].c);
	}cout << endl;
}
// vector에 대한 오른차순 정렬(default min)
bool token_comp(Token& t1, Token& t2) {
	if (t1.a != t2.a)
		// 새로 들어오는(뒤로 가는) t2는 t1보다 커야함
		return t1.a < t2.a;
	else if (t1.b != t2.b)
		return t1.b < t2.b;
	else
		return t1.c < t2.c;
}
// 우선순위큐(default max)
struct pq_comp {
	bool operator()(Token& t1, Token& t2) {
		if (t1.a != t2.a)
			// 새로 들어오는 t2가 우선순위가 높아지려면 t1보다 커야함
			return t1.a < t2.a;
		else if (t1.b != t2.b)
			return t1.b < t2.b;
		else
			return t1.c < t2.c;
	}
};

int main(int argc, char** argv) {
	vector<Token> t = { {1,2,3}, {1,1,1}, {9,22,123}, {5,10,12},{5,5,13}, {-10, 240, 777},{-10,240,0} };
	sort(t.begin(), t.end(), token_comp);
	// 결과 -> 작은것 먼저 출력
	print(t);

	priority_queue<Token, vector<Token>, pq_comp> pq;
	for (int i = 0; i < t.size(); ++i) {
		pq.push(t[i]);
	}
	// 결과 ->큰것(우선순위가 높은것) 먼저 출력
	while (!pq.empty()) {
		Token temp = pq.top();
		pq.pop();
		printf("%d %d %d\n",temp.a, temp.b, temp.c);
	}
	return 0;
}