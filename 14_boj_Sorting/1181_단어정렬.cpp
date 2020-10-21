#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

bool cmp(string& s1, string& s2) {
    // 길이가 짧은 것부터
    if (s1.length() != s2.length())
        return s1.length() < s2.length();
    // 사전순으로
    else
        return s1 < s2;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 입력
    int N;
    cin >> N;

    vector<string> arr;
    for (int i = 0; i < N; ++i) {
        string tmp;
        cin >> tmp;
        // tmp가 arr안에 없는 경우
        if (find(arr.begin(), arr.end(), tmp) == arr.end()) {
            arr.push_back(tmp);
        }
    }

    // 정렬
    sort(arr.begin(), arr.end(), cmp);

    for (vector<string>::iterator it = arr.begin(); it != arr.end(); ++it) {
        cout << *it << "\n";
    }

    return 0;
}
