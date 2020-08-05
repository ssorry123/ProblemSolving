#include<iostream>
#include<vector>

using namespace std;

int main()
{
	/* vector */
	vector<int> v1;	// ����ִ� ���� ����
	vector<int> v2(5); // 0�� 5�� ������ ���� ����
	vector<int> v3(5, 2); // 2�� 5�������� ���� ����
	vector<int> v4(v3);	// v3�� �����ؼ� v4 ����
	vector<int> v;
	v.assign(5, 2);	// 2�� ������ 5�� ���� ���Ӱ� �Ҵ�
	
	// ��ȸ ���
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
	v.pop_back();	// ������ ���� ����, void
	v.insert(v.begin(), -1); // iter�� ��ġ�ϴ� ���� -1����
	v.erase(v.begin());		// iter�� ��ġ�ϴ� ���� ���� ����

	cout << v.at(2) << endl; // 2��° ���Ұ� , ���� ����, ����, ����
	cout << v[2] << endl; // 2��° ���Ұ�, �������� x, �Ҿ���, ����
	cout << v.front() << endl;	// 0��° ���Ұ�
	cout << v.back() << endl;	// ������ ���Ұ�
	v.clear();	// ���Ҹ������, �޸� ��������


	v.begin();	// ù��° ���� ����Ŵ, iterator, �� Ȯ���� iterator �Ҵ� �� *�� ����
	v.end();	// ������ ���� ����Ŵ, iterator
	v.rbegin();  // reverse�� ����, iterator
	v.rend();  // reverse�� ������, iterator

	v.reserve(10); // n���� ���Ҹ� ���� ������(�뷮��) �����Ҵ�
	v.resize(15); // ũ�⸦ n���� ����, ��Ŀ���� ��� 0���� �ʱ�ȭ
	v.resize(20, 3); // ũ�⸦ n���� ����, �� Ŀ���� ��� 3���� �ʱ�ȭ

	v1.swap(v2);	// v1�� v2 ��� ���� ����
	vector<int>().swap(v1); // 0�� �ӽð�ü�� ����(�Ҵ�� ���� ����)


	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}