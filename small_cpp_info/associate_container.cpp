#include<iostream>
#include<set>
#include<map>
using namespace std;

int main() {
	// ���� �����̳�, 2������Ʈ���� ����, ��������� ��� ���

	// ���� �����̳� set, multiset
	set<int> s;	// set, Ű�� �ߺ� �Ұ�
	set<int>::iterator iter, start, end;
	multiset<int> ms;	// Ű �ߺ� ����
	
	start = s.begin();
	end = s.end();
	s.rbegin();
	s.rend();
	s.clear();
	s.count(1);	// ���� 1�� ���� ��ȯ
	s.empty();
	s.insert(5);	// ���� 5�� ����, ���ĵ� ��ġ�� �ڵ����� ����
	s.erase(start, end); // [start, end) ���� ����
	
	s.find(2);	// ���� 2�� iter ��ȯ, ������ s.end() �ݺ��� ��ȯ
	s.upper_bound(2);	// ���� 2�� ������ ����]�� �ݺ���
	s.lower_bound(2);	// ���� 2�� �����ϴ� ����[�� �ݺ���
	s.equal_range(2);	// ���� 2�� �����ϴ� ������ ������ ������ �ݺ��� pair
	s.value_comp();	// ���� ���� ������ ��ȯ
	s.key_comp();	// ���� ���� ������ ��ȯ
	s.size(); // ������ ���� ��ȯ
	s.max_size(); // �ִ� ������, ���� �޸� ũ�� ��ȯ

	// map, multimap
	map<int, int, greater<int>> m;	// pair<key, value> Ű �ߺ� �Ұ�
	map<int, int>::iterator iter1;
	m.insert(pair<int, int>(10, 20));
	m.insert(pair<int, int>(11, 22));
	m[10] = 23;	// key�� �ش��ϴ� value ����
	m[12] = 11;	// key, value ����, ���̽� dict�� ���
	for (iter1 = m.begin(); iter1 != m.end(); ++iter1 ) {
		cout << iter1->first <<' '<<iter1->second <<endl;
		cout << (*iter1).first << ' ' << (*iter1).second << endl;
	}

	multimap<int, int> mm; // Ű �ߺ� ����, ���۷�����[] ��� �Ұ�
	mm.upper_bound(1);	// Ű1�� upperbound)
	mm.lower_bound(1); // Ű1�� lowerbound[
	mm.equal_range(1); // Ű���� ���� pair ��ȯ [,)

	return 0;
}