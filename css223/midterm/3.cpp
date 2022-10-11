#include <iostream>
#include <string>
using namespace std;

void kangarooword(string s, string t)
{
    int s_idx = 0, t_idx = 0;

    while (s_idx < s.length() && t_idx < t.length())
    {

        if (tolower(s[s_idx]) == tolower(t[t_idx]))
        {
            s_idx++;
            t_idx++;
        }
        else
        {
            s_idx++;
        }
    }

    if (t_idx == t.length())
    {
        cout << "this is a kangaroo word";
    }
    else
    {
        cout << "this is not a kangaroo word";
    }
}

int main()
{

    string s, t;
    cout << "Enter the string line : ";
    cin >> s;
    cout << "text to find : ";
    cin >> t;
    kangarooword(s, t);

    return 0;
}
