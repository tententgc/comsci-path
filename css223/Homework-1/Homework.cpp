#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main(){ 
    ifstream inFile;
    inFile.open("mbti.csv");
    string line;
    vector<string> lines;
    while (getline(inFile, line)){
        lines.push_back(line);
    }
    inFile.close();

    for (int i = 0; i < lines.size(); i++){
        cout << lines[i] << endl;
    }
    
    
    return 0;
}