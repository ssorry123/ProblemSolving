#include<iostream>
#include<vector>

using namespace std;

int main()
{
	/* pair */
	pair<int, int> p1 = make_pair(1,2);
	cout << p1.first << ' ' << p1.second << endl;

	pair<int, int> p2(3, 4);
	cout << p2.first << ' ' << p2.second << endl;

	
	vector< pair<int, int> > v1;
	vector< pair<int, int>, pair<int, int> > v2;
	v1.push_back(pair<int, int>(5, 6));

	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}