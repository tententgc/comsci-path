#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream> 
#include <math.h>


using namespace std;

struct TypeFriend{ 
    string name; 
    double Ne; 
    double Ni; 
    double Te; 
    double Ti;
    double Se; 
    double Si; 
    double Fe;
    double Fi; 
    string type;
};

int main()
{ 
    ifstream inFile; 
    inFile.open("mbti.csv");
    string line;
    vector<string> lines;
    while (getline(inFile, line)){
        lines.push_back(line);
    }
    inFile.close();

    //push data to struct TypeFriend and split the data by comma
    vector<TypeFriend> types;
    for (int i = 0; i < lines.size(); i++){
        TypeFriend temp;
        stringstream ss(lines[i]);
        string item;
        getline(ss, item, ',');
        temp.name = item;
        getline(ss, item, ',');
        temp.Ne = stod(item);
        getline(ss, item, ',');
        temp.Ni = stod(item);
        getline(ss, item, ',');
        temp.Te = stod(item);
        getline(ss, item, ',');
        temp.Ti = stod(item);
        getline(ss, item, ',');
        temp.Se = stod(item);
        getline(ss, item, ',');
        temp.Si = stod(item);
        getline(ss, item, ',');
        temp.Fe = stod(item);
        getline(ss, item, ',');
        temp.Fi = stod(item);
        getline(ss, item, ',');
        temp.type = item;
        types.push_back(temp);
    }
    // calculate the distance between each friend and the user 
    vector<double> arr;
    for (int i = 1; i < types.size(); i++){
        double distance = 0;
        distance += pow(types[i].Ne - types[0].Ne, 2);
        distance += pow(types[i].Ni - types[0].Ni, 2);
        distance += pow(types[i].Te - types[0].Te, 2);
        distance += pow(types[i].Ti - types[0].Ti, 2);
        distance += pow(types[i].Se - types[0].Se, 2);
        distance += pow(types[i].Si - types[0].Si, 2);
        distance += pow(types[i].Fe - types[0].Fe, 2);
        distance += pow(types[i].Fi - types[0].Fi, 2);
        distance = sqrt(distance);
        arr.push_back(distance);
    }

    // sort the distance array and find the top 3 nearest friend show name and type
    vector<double> sorted = arr;
    sort(sorted.begin(), sorted.end());
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < arr.size(); j++){
            if (arr[j] == sorted[i]){
                cout << types[j].name << " " << types[j].type << endl;
            }
        }
    }

    // find my mbti type from top 3 nearest friend
    vector<string> mbti;
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < arr.size(); j++){
            if (arr[j] == sorted[i]){
                mbti.push_back(types[j].type);
            }
        }
    }
    
    



}