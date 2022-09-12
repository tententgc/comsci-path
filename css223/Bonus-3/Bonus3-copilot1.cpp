#include <iostream>
#include <string>

using namespace std;

// create scoreboard top 10 with doubly linked list
// when add newscore to scoreboard, it will be added to the right position and the lowest score will be removed

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
        while (cur != NULL)
        {
            if (cur->score < score)
            {
                newNode->next = cur;
                newNode->prev = cur->prev;
                cur->prev->next = newNode;
                cur->prev = newNode;
                count++;
                return;
            }
            cur = cur->next;
        }
    }
    void printScoreBoard()
    {
        Node* cur = head;
        cout << "ScoreBoard" << endl;
        cout << "----------" << endl;
        while (cur != NULL)
        {
            cout << cur->name << " : " << cur->score << endl;
            cur = cur->next;
        }
        cout << "----------" << endl;
    }
};

int main()
{
    ScoreBoard* scoreboard = new ScoreBoard();
    scoreboard->addScore(100, "A");
    scoreboard->addScore(50, "B");
    scoreboard->addScore(200, "C");
    scoreboard->addScore(150, "D");
    scoreboard->addScore(300, "E");
    scoreboard->addScore(250, "F");
    scoreboard->addScore(400, "G");
    scoreboard->addScore(350, "H");
    scoreboard->addScore(500, "I");
    scoreboard->addScore(450, "J");
    scoreboard->addScore(600, "K");
    scoreboard->addScore(550, "L");
    scoreboard->addScore(700, "M");
    scoreboard->printScoreBoard();
    return 0;
}