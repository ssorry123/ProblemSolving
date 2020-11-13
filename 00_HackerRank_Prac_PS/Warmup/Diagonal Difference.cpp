#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

int diagonalDifference(vector<vector<int>> arr) {
    int a = 0, b = 0;
    int n = arr.size();
    for(int i = 0; i < n; ++i){
        a += arr[i][i];
        b += arr[i][n - i - 1];
    }
    return abs(a - b);
}