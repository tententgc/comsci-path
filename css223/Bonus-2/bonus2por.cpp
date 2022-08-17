#include <iostream>
#include <cstdlib>
#include <math.h>

using namespace std;

struct students
{
    string name;
    int score;
} student[10];

string FindMax(students student[10])
{
    string maxname = student[0].name;
    int maxscore = student[0].score;
    for (int i = 1; i < 10; i++)
    {
        if (student[i].score > maxscore)
        {
            maxscore = student[i].score;
            maxname = student[i].name;
        }
    }
    return maxname;
}

int main()
{
    string name[10] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
    int score[10] = {4, 25, 55, 55, 57, 60, 66, 67, 68, 83};
    for (int i = 0; i <= 10; i++)
    {
        student[i].name = name[i];
        student[i].score = score[i];
    }
    cout << FindMax(student) << endl;
}
