#include <iostream> 

using namespace std; 

string mergesort(string s)
{ 
    if(s.length() == 1){
        return s;
    }
    string s1 = s.substr(0, s.length()/2);
    string s2 = s.substr(s.length()/2, s.length());
    s1 = mergesort(s1);
    s2 = mergesort(s2);
    int i = 0, j = 0, k = 0;
    while(i < s1.length() && j < s2.length()){
        if(s1[i] < s2[j]){
            s[k] = s1[i];
            i++;
        }
        else{
            s[k] = s2[j];
            j++;
        }
        k++;
    }
    while(i < s1.length()){
        s[k] = s1[i];
        i++;
        k++;
    }
    while(j < s2.length()){
        s[k] = s2[j];
        j++;
        k++;
    }
    return s;
}



int main(){ 
    string s_lower, t_lower; 
    string s;
    cin >> s;
    for (int i = 0; i < s.length(); i++)
    {
        s_lower += tolower(s[i]);
    }

    string t;
    cin >> t;
    for (int i = 0; i < t.length(); i++)
    {
        t_lower += tolower(t[i]);
    } 
    
    s = mergesort(s_lower);
    t =  mergesort(t_lower); 
    if(s == t){
        cout << "The words are anagrams";
    }
    else{
        cout << "The words are not anagrams";
    }
}