#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the plusMinus function below.
void plusMinus(vector<int> arr) {
    int pnum, mnum, znum;
    pnum = mnum = znum = 0;
    
    for (int i=0; i<arr.size(); ++i){
        int tmp = arr[i];
        if (tmp > 0)
            ++pnum;
        else if (tmp < 0)
            ++mnum;
        else
            ++znum;
    }
    
    double total = (double)arr.size();
    
    cout << fixed;      // 소수점 아래
    cout.precision(6);  // 6자리
    
    cout << pnum / total << '\n';
    cout << mnum / total << '\n';
    cout << znum / total << '\n';
    
}