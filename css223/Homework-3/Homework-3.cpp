#include <iostream>
#include <string>  

using namespace std;


void sort(int arr[][3], int n) {
    int temp[3];
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (arr[i][0] > arr[j][0]) {
                temp[0] = arr[i][0];
                temp[1] = arr[i][1];
                temp[2] = arr[i][2];
                arr[i][0] = arr[j][0];
                arr[i][1] = arr[j][1];
                arr[i][2] = arr[j][2];
                arr[j][0] = temp[0];
                arr[j][1] = temp[1];
                arr[j][2] = temp[2];
            }
            else if (arr[i][0] == arr[j][0]) {
                if (arr[i][1] > arr[j][1]) {
                    temp[0] = arr[i][0];
                    temp[1] = arr[i][1];
                    temp[2] = arr[i][2];
                    arr[i][0] = arr[j][0];
                    arr[i][1] = arr[j][1];
                    arr[i][2] = arr[j][2];
                    arr[j][0] = temp[0];
                    arr[j][1] = temp[1];
                    arr[j][2] = temp[2];
                }
                else if (arr[i][1] == arr[j][1]) {
                    if (arr[i][2] > arr[j][2]) {
                        temp[0] = arr[i][0];
                        temp[1] = arr[i][1];
                        temp[2] = arr[i][2];
                        arr[i][0] = arr[j][0];
                        arr[i][1] = arr[j][1];
                        arr[i][2] = arr[j][2];
                        arr[j][0] = temp[0];
                        arr[j][1] = temp[1];
                        arr[j][2] = temp[2];
                    }
                }
            }
        }
    }
}

int main() {
    int arr[9][3] = {{1,2,3},{1,2,2},{1,1,1},{2,2,2},{2,1,1},{2,1,2},{3,3,3},{3,2,2},{3,1,1}};
    cout << "Before sorting" << endl;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 3; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    cout << "After sorting" << endl;
    sort(arr, 9);
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 3; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

