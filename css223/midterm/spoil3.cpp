#include <iostream> 
#include <vector> 
#include <string>

using namespace std; 

int findtext(string str,string txt)
{
    int i,j;
    int n=str.length();
    int m=txt.length();
    for(i=0;i<n-m;i++)
    {
        for(j=0;j<m;j++)
        {
            if(str[i+j]!=txt[j])
            {
                break;
            }
        }
        if(j==m)
        {
            return i;
        }
    }
    return -1;
}

//find txt in str and show the result if found
void findAndShow(string str, string txt)
{
    int found = findtext(str, txt);
    if (found != string::npos)
        cout << "Found " << txt << " at position " << found << endl;
    else
        cout << "Not found " << txt << endl;
}

int main() 
{ 
    string str = "Hello, world!";
    string txt = "world";
    findAndShow(str, txt);
    txt = "World";
    findAndShow(str, txt);
    return 0; 
}
