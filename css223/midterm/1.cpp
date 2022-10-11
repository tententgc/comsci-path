#include <iostream> 

using namespace std;
#include <iostream>

using namespace std;

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];


    i = 0; 
    j = 0;
    k = l; 
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }


    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }


    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergesort(int a[], int low, int high)
{
    int mid;
    if (low < high)
    {
        mid = (low + high) / 2;
        mergesort(a, low, mid);
        mergesort(a, mid + 1, high);
        merge(a, low, mid, high);
    }
}


int main()
{
    int a[] = {1, 9, 8, 5, 3, 4, 2, 6, 7, 0,100,-1,-100};
    int len = sizeof(a) / sizeof(a[0]);
    mergesort(a, 0, len);


    int n;
    cin >> n;

    //show min n value
    cout << "show min number" << endl; 
    for (int i = 0; i < n; i++)
    {
        cout << a[i]<<" "; 
    }

    cout << endl;

    return 0;
}


//BigO(nlogn)