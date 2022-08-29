#include <iostream>
#include <ctime>
#include <cstdlib>
#include <math.h>

using namespace std;

struct Students
{
    string name;
    int score;
} student[10];

string Maxstudentscore(Students student[10])
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

string Minstudentscore(Students student[10])
{
    string minname = student[0].name;
    int minscore = student[0].score;
    for (int i = 1; i < 10; i++)
    {
        if (student[i].score < minscore)
        {
            minscore = student[i].score;
            minname = student[i].name;
        }
    }
    return minname;
}

double Average(Students student[10])
{
    double sum = 0;
    for (int i = 0; i < 10; i++)
    {
        sum += student[i].score;
    }
    return sum / 10;
}

int Modescore(Students student[10])
{
    int mode = 0;
    int count = 0;
    int maxcount = 0;
    for (int i = 0; i < 10; i++)
    {
        count = 0;
        for (int j = 0; j < 10; j++)
        {
            if (student[i].score == student[j].score)
            {
                count++;
            }
        }
        if (count > maxcount)
        {
            maxcount = count;
            mode = student[i].score;
        }
    }
    return mode;
}

double MedianScore(Students student[10])
    {
        double median = 0;
        int count = 0;
        for (int i = 0; i < 10; i++)
        {
            count++;
        }
        if (count % 2 == 0)
        {
            median = (student[count / 2].score + student[count / 2 - 1].score) / 2;
        }
        else
        {
            median = student[count / 2].score;
        }
        return median;
    }

double SDscore(Students student[10])
    {
        double sum = 0;
        double mean = Average(student);
        for (int i = 0; i < 10; i++)
        {
            sum += pow(student[i].score - mean, 2);
        }
        return sqrt(sum / 10);
    }

void ShowgradeAllstudents(Students student[10], double avg, double sd)
    {
        for (int i = 0; i < 10; i++)
        {
            if (student[i].score > avg + (2 * sd))
            {
                cout << student[i].name << ": A" << endl;
            }
            else if (student[i].score > avg + sd)
            {
                cout << student[i].name << ": B" << endl;
            }
            else if (student[i].score > avg)
            {
                cout << student[i].name << ": C" << endl;
            }
            else if (student[i].score > avg - sd)
            {
                cout << student[i].name << ": D" << endl;
            }
            else
            {
                cout << student[i].name << ": F" << endl;
            }
        }
    }

int main()
    {
        string name[10] = {"John", "Mary", "Peter", "Tenten", "Rew", "Jenny", "Tom", "Jerry", "Jack", "Lily"};
        int score[10] = {80, 99, 58, 66, 66, 55, 42, 31, 72, 51};

        for (int i = 0; i < 10; i++)
        {
            student[i].name = name[i];
            student[i].score = score[i];
        }

        double avg = Average(student);
        double sd = SDscore(student);
        cout << "The highest score is " << Maxstudentscore(student) << endl;
        cout << "The lowest score is " << Minstudentscore(student) << endl;
        cout << "The average score is " << avg << endl;
        cout << "The mode score is " << Modescore(student) << endl;
        cout << "The median score is " << MedianScore(student) << endl;
        cout << "The standard deviation score is " << sd << endl;
        ShowgradeAllstudents(student, avg, sd);
    }
