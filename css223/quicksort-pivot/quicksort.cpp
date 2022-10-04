#include <iostream> 

using namespace std;

void quicksort(int arr[], int start , int end){
    if(start >= end){
        return;
    }
    int pivot = arr[start];
    int i = start;
    int j = end;
    
    while(i < j){
        while(i < j && arr[j] >= pivot){
            j--;
        }
        if(i < j){
            arr[i] = arr[j];
            i++;
        }
        while(i < j && arr[i] <= pivot){
            i++;
        }
        if(i < j){
            arr[j] = arr[i];
            j--;
        }

    }
    arr[i] = pivot;
    quicksort(arr, start, i-1);
    quicksort(arr, i+1, end);
}

int main(){
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int start = 0;
    int end = 9;
    quicksort(arr, start, end);
    for(int i = 0; i < 10; i++){
        cout << arr[i] << " ";
    }
    return 0;
}