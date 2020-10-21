#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool cmp(char& a, char& b) {
    return a > b;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    char str[11];
    cin >> str;

    // 길이 측정
    int len = 0;
    char* p = str;
    while (*p != NULL) {
        ++len;
        ++p;
    }
    
    // 내림차순 정렬
    sort(str, str + len, cmp);

    // 출력
    cout << str;

    return 0;
}
