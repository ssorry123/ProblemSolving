#include<iostream>
#include<algorithm>
#include<vector>
#include<ctime>

using namespace std;

void print_array(int* arr);
void print_array(const vector<int>& v);

int main() {

	int arr[10] = {34, 123,144, 1, -15, 100, 77, 121, 0, 121};
	print_array(arr);
	sort(arr, arr + 10);	// 기본 정렬(오름차순)
	print_array(arr);

	sort(arr, arr + 10, greater<int>());	// 내림차순 정렬
	print_array(arr);

	vector<int> v;
	for (int i = 0; i < 10; i++) {
		v.push_back(rand() % 200);
	}
	print_array(v);
	sort(v.begin(), v.end());
	print_array(v);

	return 0;
}

void print_array(int* arr) {
	cout << "arr" << endl;
	int arrSize = sizeof(arr) / sizeof(int);
	for (int i = 0; i < arrSize; ++i) {
		cout << arr[i] << ' ';
	}cout << endl;
}

void print_array(const vector<int>& v) {
	int arrSize = v.size();
	cout << "arr" << endl;

	for (int i = 0; i < arrSize; ++i) {
		cout << v[i] << ' ';
	}cout << endl;
	
}
