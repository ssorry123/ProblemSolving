#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <cmath>

using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    while (true) {
        vector<int> arr(3);
        cin >> arr[0] >> arr[1] >> arr[2];
        if (arr[0] == 0 && arr[0]==arr[1] && arr[1]==arr[2]) 
            break;

        sort(arr.begin(), arr.end());
        int c2 = pow(arr[2], 2);
        int a2b2 = pow(arr[1], 2) + pow(arr[0], 2);

        if (a2b2 == c2)
            cout << "right\n";
        else
            cout << "wrong\n";

    }

    return 0;
}
