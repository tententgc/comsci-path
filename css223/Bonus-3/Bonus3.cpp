#include <iostream> 
#include <string>
using namespace std;

//create scoreboard top 10 with doubly linked list
// when add newscore to scoreboard, it will be added to the right position
// and the lowest score will be removed

class Node
{
public:
    Node* next;
    Node* prev;
    int score;
    string name;
    Node(int score, string name)
    {
        this->score = score;
        this->name = name;
        next = NULL;
        prev = NULL;
    }
};

class ScoreBoard
{
public:
    Node* head;
    Node* tail;
    int count;
    ScoreBoard()
    {
        head = NULL;
        tail = NULL;
        count = 0;
    }
    void addScore(int score, string name)
    {
        Node* newNode = new Node(score, name);
        Node* cur = head;
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
    void printScoreBoard()
    {
        Node* cur = head;
        int i = 1;
        while (cur != NULL)
        {
            cout << i << ". " << cur->name << " : " << cur->score << endl;
            cur = cur->next;
            i++;
        }
    }
};

int main()
{
    ScoreBoard* s = new ScoreBoard();
    s->addScore(100, "aaa");
    s->addScore(200, "bbb");
    s->addScore(150, "ccc");
    s->addScore(250, "ddd");
    s->addScore(300, "eee");
    s->addScore(50, "fff");
    s->addScore(400, "ggg");
    s->addScore(350, "hhh");
    s->addScore(450, "iii");
    s->addScore(500, "jjj");
    
    s->addScore(460,"gjs");
    s->addScore(470, "gjs");
    s->printScoreBoard();
}

//Big O: O(n)