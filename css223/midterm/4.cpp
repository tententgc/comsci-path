#include <iostream>

using namespace std; 


int main()
{ 
    string word1, word2; 
    cout << "Enter the first word: ";
    cin >> word1;
    cout << "Enter the second word: ";
    cin >> word2;

    if(word1.length() != word2.length()){
        cout << "The words are not anagrams";
        return 0;
    }

    
    
    int cnt1[26] = {0};
    int cnt2[26] = {0};

    for(int i = 0; i < word1.length(); i++){
        word1[i] = tolower(word1[i]);
        word2[i] = tolower(word2[i]);
        cnt1[word1[i] - 'a']++;
        cnt2[word2[i] - 'a']++;
    } 

    for(int i = 0; i < 26; i++){
        if(cnt1[i] != cnt2[i]){
            cout << "The words are not anagrams";
            return 0;
        }
    }

    cout << "The words are anagrams"; 

    return 0;
}