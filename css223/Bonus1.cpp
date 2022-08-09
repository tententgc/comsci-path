#include <iostream> 
#include <ctime> 
#include <cstdlib>
#include <math.h>

// any, any
// 6,4
// 4,0

using namespace std;
int main() {

    srand((unsigned)time(0));
    int tree[2] = {rand()%10, rand()%10};
    int hero[2] = {6,4}; 
    int monster[2] = {4,0}; 

    for (int i =0 ; i<10 ; i++ ){ 
        cout<< endl;
        for(int j=0 ; j<10 ;  j++){ 
            if (i == tree[0] && j == tree[1]){
                cout << 1;
            }
            else if (i == hero[0] && j == hero[1]){
                cout << 2;
            }
            else if (i == monster[0] && j == monster[1]){
                cout << 3;
            }
            else {
                cout << 0;
            }
        }
    }
    cout << endl ; 


    int Taxicab = abs(4-6) + abs(0-4);
    cout << "Taxicab: " << Taxicab << endl;

    double Euclidean = sqrt(pow(4-6,2) + pow(0-4,2)); 
    cout << "Euclidean: " << Euclidean << endl; 

    double Chebyshev = max(abs(4-6), abs(0-4));
    cout << "Chebyshev: " << Chebyshev << endl; 
}