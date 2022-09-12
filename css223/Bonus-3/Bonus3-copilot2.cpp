#include <iostream> 
#include <string>

using namespace std;

// create scoreboard top 10 with doubly linked list and when add newscore to scoreboard, it will be added to the right position and the lowest score will be removed

struct Node
{
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

        if (count == 10)
        {
            tail = tail->prev;
            tail->next = NULL;
            count--;
        }

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
            return;
        }
        while (cur->next != NULL && cur->next->score > score)
        {
            cur = cur->next;
        }
        newNode->next = cur->next;
        cur->next = newNode;
        newNode->prev = cur;
        newNode->next->prev = newNode;
        count++;
        return;
    }
    void printScoreBoard()
    {
        Node* cur = head;
        while (cur != NULL)
        {
            cout << cur->name << " " << cur->score << endl;
            cur = cur->next;
        }
    }
};

int main()
{
    ScoreBoard* sb = new ScoreBoard();
    sb->addScore(5, "a");
    sb->addScore(6, "b");
    sb->addScore(7, "c");
    sb->addScore(8, "d");
    sb->addScore(9, "e");
    sb->addScore(10, "f");
    sb->addScore(11, "g");
    sb->addScore(12, "h");
    sb->addScore(13, "i");
    sb->addScore(14, "j");
    sb->addScore(15, "k");
    sb->printScoreBoard();
    return 0;
}
