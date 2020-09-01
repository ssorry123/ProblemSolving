#include<iostream>
#include<vector>

using namespace std;

int main()
{
	/* vector */
	vector<int> v1;	// 비어있는 벡터 생성
	vector<int> v2(5); // 0을 5개 가지는 벡터 생성
	vector<int> v3(5, 2); // 2를 5개가지는 벡터 생성
	vector<int> v4(v3);	// v3을 복사해서 v4 생성
	vector<int> v;
	v.assign(5, 2);	// 2의 값으로 5개 원소 새롭게 할당
	
	// 순회 방법
	v = { 1,2,3,4,5,6 };
	for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
		cout << *it << ' ';
	}cout << endl;
	for (vector<int>::reverse_iterator it = v.rbegin(); it != v.rend(); ++it) {
		cout << *it << ' ';
	}cout << endl;
	for (int i = 0; i < v.size(); ++i) {
		cout << v[i] << ' ';
	}cout << endl;

	v.push_back(7); // append(7), void,
	v.pop_back();	// 마지막 원소 제거, void
	v.insert(v.begin(), -1); // iter가 위치하는 곳에 -1삽입
	v.erase(v.begin());		// iter가 위치하는 곳의 원소 제거

	cout << v.at(2) << endl; // 2번째 원소값 , 범위 점검, 안전, 느림
	cout << v[2] << endl; // 2번째 원소값, 범위점검 x, 불안전, 빠름
	cout << v.front() << endl;	// 0번째 원소값
	cout << v.back() << endl;	// 마지막 원소값
	v.clear();	// 원소모두제거, 메모리 남아있음


	v.begin();	// 첫번째 원소 가리킴, iterator, 값 확인은 iterator 할당 후 *로 참조
	v.end();	// 마지막 원소 가리킴, iterator
	v.rbegin();  // reverse의 시작, iterator
	v.rend();  // reverse의 마지막, iterator

	v.reserve(10); // n개의 원소를 위한 공간만(용량만) 동적할당
	v.resize(15); // 크기를 n으로 변경, 더커지는 경우 0으로 초기화
	v.resize(20, 3); // 크기를 n으로 변경, 더 커지는 경우 3으로 초기화

	v1.swap(v2);	// v1과 v2 모든 것을 스왑
	vector<int>().swap(v1); // 0인 임시객체와 스왑(할당된 공간 제거)


	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}