#include <iostream> 

using namespace std; 

string checkinstring(string s ,string t){
    while(s.length() != 0){
        if(s[0] == t[0]){
            s.erase(0,1);
            t.erase(0,1);
        }else{
            s.erase(0,1);
        }

        if(t.length() == 0){
            return "this is a kangaroo word";
        }
    }
    return "this is not a kangaroo word";
}
int main(){
    string s, t;
    cout << "Enter the string line : ";
    cin >> s;
    cout << "text to find : ";
    cin >> t;
    cout << checkinstring(s, t);
    return 0;
}
