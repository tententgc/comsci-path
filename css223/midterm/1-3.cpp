#include <iostream>
#include <string>
using namespace std;

class Node
{
public:
    Node *next;
    Node *prev;
    int score;
    Node(int score)
    {
        this->score = score;
        next = NULL;
        prev = NULL;
    }
};

class ScoreBoard
{
public:
    Node *head;
    Node *tail;
    int count;
    ScoreBoard()
    {
        head = NULL;
        tail = NULL;
        count = 0;
    }
    void addScore(int score)
    {
        Node *newNode = new Node(score);
        Node *cur = head;
        if (head == NULL)
        {
            head = newNode;
            tail = newNode;
            count++;
            return;
        }
        if (head->score < score)
        {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
            count++;
            return;
        }
        if (tail->score > score)
        {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
            count++;
            if (count > 10)
            {
                tail = tail->prev;
                tail->next = NULL;
            }
            return;
        }
        while (cur->next != NULL)
        {
            if (cur->next->score < score)
            {
                newNode->next = cur->next;
                cur->next->prev = newNode;
                cur->next = newNode;
                newNode->prev = cur;
                count++;
                if (count > 10)
                {
                    tail = tail->prev;
                    tail->next = NULL;
                }
                return;
            }
            else
            {
                cur = cur->next;
            }
        }
    }


    void printScoreBoard(int n)
    {
        Node *cur = head;
        int i = 1;
        for (i = 1; i <= n; i++)
        {
            if (cur == NULL)
            {
                break;
            }
            cout << cur->score << " ";
            cur = cur->next;
        }
    }
};


int main(){
    int arr[] = {100,78,79,85,14,25,16,7,8,0,-1,-2}; 
    int n = sizeof(arr)/sizeof(arr[0]); 

    ScoreBoard *scoreBoard = new ScoreBoard();
    for(int i=0;i<n;i++){
        scoreBoard->addScore(arr[i]);
    }
    int top; 
    cout << "Enter top value you want to show : ";
    cin >> top;
    scoreBoard->printScoreBoard(top);
}

//Big O: O(n)
// ใช้ Linked list ขอข้อสกอร์บอร์ดที่เป็นโบนัสมาแก้แล้วให้ linked list วนแอดค่า top score ออกมมา
// input ที่ใส่ตรง Enter top value you want to show : คือ n ตัว ซึ่งไม่เกิน 12 เพราะ ผมสร้าง array เก็บค่า 12 ตัว ก่อนโยนเข้าไป sort
