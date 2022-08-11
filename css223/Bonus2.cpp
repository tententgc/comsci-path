#include <iostream>
#include <ctime> 
#include <cstdlib> 
#include <math.h>

using namespace std;
int main(){ 
    int map[10][10]; 
    
    for(int i=0; i<10; i++){
        for(int j=0; j<10; j++){
            map[i][j] = 0;
        }
    } 

    int hero[2] = {6,4};
    int monster[2] = {4,0};
    
    map[hero[0]][hero[1]] = 2; 
    map[monster[0]][monster[1]] = 3; 

    srand((unsigned)time(0));
    int tree[2] = {rand()%10, rand()%10}; 

    map[tree[0]][tree[1]] = 1; 

    for (int i=0; i<10; i++){
        for (int j=0; j<10; j++){
            cout << map[i][j] << " ";
        }
        cout << endl;
    }



    int Taxicab = abs(4 - 6) + abs(0 - 4);
    cout << "Taxicab: " << Taxicab << endl;

    double Euclidean = sqrt(pow(4 - 6, 2) + pow(0 - 4, 2));
    cout << "Euclidean: " << Euclidean << endl;

    double Chebyshev = max(abs(4 - 6), abs(0 - 4));
    cout << "Chebyshev: " << Chebyshev << endl;
}