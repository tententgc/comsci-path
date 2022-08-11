#include <iostream>

using namespace std;
int main(){
    int x=0,y=1,q=0; 
    for (int i=0; i<100 ; i++){
        q = x + y;
        x=y; 
        y = q ;
        i = q;
        cout << q << endl; 
    }
}