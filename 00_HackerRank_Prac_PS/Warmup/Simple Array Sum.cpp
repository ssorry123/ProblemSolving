#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

/*
 * Complete the simpleArraySum function below.
 */
int simpleArraySum(vector<int> ar) {
    /*
     * Write your code here.
     */
    int ret = 0;
    for(int i = 0; i < ar.size(); ++i){
        ret += ar[i];
    }
    return ret;
}
