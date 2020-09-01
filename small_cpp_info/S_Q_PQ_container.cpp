#include<iostream>
#include<stack>
#include<queue>

using namespace std;

int main() {
	stack<int> s1;
	stack<pair<int, int>> s2;
	s1.empty();	// 비었는지 확인
	s1.size(); // 사이즈 반환
	s1.push(1);
	s1.top(); // 가장 위의 데이터 반환
	s1.pop(); // 가장 위의 데이터 삭제, void

	s2.push(make_pair(1, 2));
	cout << s2.top().first<< ' ' << s2.top().second << endl;

	queue<int> q1;
	q1.empty();
	q1.size();
	q1.push(3);
	q1.front();
	q1.back();
	q1.pop();	// void
	
	priority_queue<int> pq1;
	pq1.empty();
	pq1.size();
	pq1.push(1);
	pq1.top();
	pq1.pop();	// void

	return 0;
}