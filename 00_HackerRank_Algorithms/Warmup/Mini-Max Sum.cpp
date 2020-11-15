#include <bits/stdc++.h>
#include <stdint.h>
#include <algorithm>

using namespace std;

vector<string> split_string(string);

// Complete the miniMaxSum function below.
void miniMaxSum(vector<int> arr) {
    sort(arr.begin(), arr.end());
    int64_t sum = 0;
    for(int i=0;i<arr.size();++i){
        sum += arr[i];
    }
    
    cout << sum - arr[arr.size()-1] << " "
        << sum - arr[0] << endl;
    
}
