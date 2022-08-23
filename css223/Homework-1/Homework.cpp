#include <iostream>
#include <string>
#include <vector>
#include <fstream> // for file input file to read csv file

using namespace std; 

int main(){
    
    string myFilePath = "./mbti.csv";
    ifstream myFile(myFilePath); // open file
    string line;
    vector<string> myVector;
    
    while(getline(myFile, line)){ // read line by line
        myVector.push_back(line);
    }
    myFile.close(); // close file


    return 0; 
}