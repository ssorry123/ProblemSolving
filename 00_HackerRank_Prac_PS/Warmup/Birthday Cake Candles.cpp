#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'birthdayCakeCandles' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY candles as parameter.
 */

int birthdayCakeCandles(vector<int> candles) {
    sort(candles.begin(), candles.end());
    int max_value = candles.back();
    
    int ret = 0;
    for (int i = candles.size()-1; i>=0; --i){
        if (max_value == candles[i]){
            ++ret;
        }
        else{
            break;
        }
    }
    return ret;
}