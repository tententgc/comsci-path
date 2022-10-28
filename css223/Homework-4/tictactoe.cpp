#include <iostream>
#include <string>
#include <vector> 
#include <algorithm> 
#include <cstdlib> 
#include <ctime>
#include <cmath> 

using namespace std; 

int main(){
    int n;
    cin >> n;
    int a[n][n];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> a[i][j];
        }
    }
    int sum = 0;
    for(int i = 0; i < n; i++){
        sum += a[i][i];
    }
    int sum2 = 0;
    for(int i = 0; i < n; i++){
        sum2 += a[i][n - i - 1];
    }
    cout << abs(sum - sum2);
    return 0;
}