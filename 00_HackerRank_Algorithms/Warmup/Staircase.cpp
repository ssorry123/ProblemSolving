#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.

void space(int n){
    for (int i=0; i<n ;++i)
        cout << " ";
}
void sharp(int n){
    for (int i=0; i<n ;++i)
        cout << "#";
}

void staircase(int n) {
    for (int i=1; i<=n; ++i){
        space(n-i);
        sharp(i);
        cout << "\n";
    }

}