#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

struct
{                    
    string name;
    double Ne;
    double Ni;
    double Te;
    double Ti;
    double Se;
    double Si; 
    double Fe;
    double Fi;
    string Type;
} Element;

int main(){ 
    ifstream inFile;
    inFile.open("mbti.csv");
    string line;
    vector<string> lines;
    while (getline(inFile, line)){
        lines.push_back(line);
    }
    inFile.close();
    
    return 0;
}