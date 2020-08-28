#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

#define MAX 1000	// 문자열의 최대 길이
int N;				// 전깃줄의 개수 <= 100

int LCS[1 + MAX][1 + MAX];
string s1;
string s2;

int main(int argc, char** argv) {
	cin >> s1;
	cin >> s2;

	for (int a = 1; a <= s1.length(); ++a) {
		for (int b = 1; b <= s2.length(); ++b) {
			if (s1[a-1] == s2[b-1]) {
				LCS[a][b] = LCS[a - 1][b - 1] + 1;
			}
			else {
				LCS[a][b] = max(LCS[a - 1][b], LCS[a][b - 1]);
			}
		}
	}

	//for (int a = 0; a <= s1.length(); ++a) {
	//	for (int b = 0; b <= s2.length(); ++b) {
	//		cout << LCS[a][b] << " ";
	//	}cout << endl;
	//}

	cout << LCS[s1.length()][s2.length()] << endl;

	return 0;
}