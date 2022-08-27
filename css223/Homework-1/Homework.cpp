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

    
    string Typeout[3] = {};
    double minnum = arr[0]; 
    string nameOut = types[0].name; 
    Typeout[0] = types[0].type; 

    for (int i = 0; i < arr.size(); i++){ 
        if (arr[i] < minnum){ 
            minnum = arr[i]; 
            Typeout[0] = types[i].type; 
            nameOut = types[i].name; 
        } 
    }
    cout << nameOut << " is a " << Typeout[0] << endl;



    double check = minnum;
    double minnum2 = arr[0];

    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] < minnum2 and arr[i] > check)
        {
            minnum2 = arr[i];
            Typeout[1] = types[i].type;
            nameOut = types[i].name;
        }
    }
    cout << nameOut << " is a " << Typeout[1] << endl;

    double check2 = minnum2;
    double minnum3 = arr[0];
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] < minnum3 and arr[i] > check2)
        {
            minnum3 = arr[i];
            Typeout[2] = types[i].type;
            nameOut = types[i].name;
        }
    }
    cout << nameOut << " is a " << Typeout[2] << endl;

    //create my type from Typeout and print out my type
    string myType = "";
    int count[4] = {0,0,0,0};
    for (int i = 0; i < 3; i++)
    {
        if (Typeout[i][0] == 'E'){ 
            count[0]++; 
        }
        else if (Typeout[i][0] == 'I'){
            count[0]++;
        }

        if (Typeout[i][1] == 'S'){
            count[1]++;
        }
        else if (Typeout[i][1] == 'N'){
            count[1]++;
        }

        if (Typeout[i][2] == 'T'){
            count[2]++;
        }
        else if (Typeout[i][2] == 'F'){
            count[2]++;
        }

        if (Typeout[i][3] == 'J'){
            count[3]++;
        }
        else if (Typeout[i][3] == 'P'){
            count[3]++;
        }
    } 

    if (count[0]>1){
        myType += "E";
    }
    else{ 
        myType += "I";
    }

    if (count[1]>1){
        myType += "S";
    }
    else{
        myType += "N";
    }

    if (count[2]>1){
        myType += "T";
    }
    else{
        myType += "F";
    }

    if (count[3]>1){
        myType += "J";
    }
    else{
        myType += "P";
    }

    cout << "My type is " << myType << endl;

}