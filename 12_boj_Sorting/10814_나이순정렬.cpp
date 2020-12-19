#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

typedef struct _info {
    int age;
    string name;
    int code;
}info;

bool cmp(info& a, info& b) {
    // 나이순
    if (a.age != b.age)
        return a.age < b.age;
    // 가입한 순서순
    else
        return a.code < b.code;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 입력
    int N;
    cin >> N;
    vector<info> arr;
    for (int i = 0; i < N; ++i) {
        int age;
        string name;
        cin >> age >> name;
        arr.push_back({ age, name, i });
    }
    
    // 정렬
    sort(arr.begin(), arr.end(), cmp);

    // 출력
    for (int i = 0; i < N; ++i) {
        cout << arr[i].age << " " << arr[i].name << "\n";
    }

    return 0;
}
