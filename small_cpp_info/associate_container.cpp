#include<iostream>
#include<set>
#include<map>
using namespace std;

int main() {
	// 연관 컨테이너, 2진균형트리로 구현, 멤버변수가 모두 비슷

	// 연관 컨테이너 set, multiset
	set<int> s;	// set, 키값 중복 불가
	set<int>::iterator iter, start, end;
	multiset<int> ms;	// 키 중복 가능
	
	start = s.begin();
	end = s.end();
	s.rbegin();
	s.rend();
	s.clear();
	s.count(1);	// 원소 1의 갯수 반환
	s.empty();
	s.insert(5);	// 원소 5를 삽입, 정렬된 위치에 자동으로 삽입
	s.erase(start, end); // [start, end) 원소 제거
	
	s.find(2);	// 원소 2의 iter 반환, 없으면 s.end() 반복자 반환
	s.upper_bound(2);	// 원소 2가 끝나는 구간]의 반복자
	s.lower_bound(2);	// 원소 2가 시작하는 구간[의 반복자
	s.equal_range(2);	// 원소 2가 시작하는 구간과 끝나는 구간의 반복자 pair
	s.value_comp();	// 정렬 기준 조건자 반환
	s.key_comp();	// 정렬 기준 조건자 반환
	s.size(); // 원소의 갯수 반환
	s.max_size(); // 최대 사이즈, 남은 메모리 크기 반환

	// map, multimap
	map<int, int, greater<int>> m;	// pair<key, value> 키 중복 불가
	map<int, int>::iterator iter1;
	m.insert(pair<int, int>(10, 20));
	m.insert(pair<int, int>(11, 22));
	m[10] = 23;	// key에 해당하는 value 수정
	m[12] = 11;	// key, value 삽입, 파이썬 dict와 비슷
	for (iter1 = m.begin(); iter1 != m.end(); ++iter1 ) {
		cout << iter1->first <<' '<<iter1->second <<endl;
		cout << (*iter1).first << ' ' << (*iter1).second << endl;
	}

	multimap<int, int> mm; // 키 중복 가능, 오퍼레이터[] 사용 불가
	mm.upper_bound(1);	// 키1의 upperbound)
	mm.lower_bound(1); // 키1의 lowerbound[
	mm.equal_range(1); // 키값의 범위 pair 반환 [,)

	return 0;
}