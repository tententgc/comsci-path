#include <iostream>
#include <string>

using namespace std;

// create scoreboard top 10 with doubly linked list
// when add newscore to scoreboard, it will be added to the right position and the lowest score will be removed
// when print scoreboard, it will be printed from highest to lowest score

struct node
{
    string name;
    int score;
    node *next;
    node *prev;
};

class Scoreboard
{
    private:
        node *head;
        node *tail;
        int size;
    public:
        Scoreboard();
        void addScore(string name, int score);
        void printScoreboard();
};

Scoreboard::Scoreboard()
{
    head = NULL;
    tail = NULL;
    size = 0;
}

void Scoreboard::addScore(string name, int score)
{
    node *temp = new node;
    temp->name = name;
    temp->score = score;
    temp->next = NULL;
    temp->prev = NULL;

    if (head == NULL)
    {
        head = temp;
        tail = temp;
    }
    else
    {
        node *current = head;
        while (current != NULL && score < current->score)
        {
            current = current->next;
        }
        if (current == NULL)
        {
            temp->next = head;
            head->prev = temp;
            head = temp;
        }
        else if (current->prev == NULL)
        {
            temp->next = current;
            current->prev = temp;
            head = temp;
        }
        else
        {
            temp->prev = current->prev;
            current->prev->next = temp;
            temp->next = current;
            current->prev = temp;
        }
    }
    size++;
    if (size > 10)
    {
        node *temp = tail;
        tail = tail->prev;
        tail->next = NULL;
        delete temp;
        size--;
    }
}

void Scoreboard::printScoreboard()
{
    node *current = head;
    while (current != NULL)
    {
        cout << current->name << " " << current->score << endl;
        current = current->next;
    }
}

int main()
{
    Scoreboard scoreboard;
    scoreboard.addScore("John", 100);
    scoreboard.addScore("Mary", 200);
    scoreboard.addScore("Jack", 300);
    scoreboard.addScore("Bob", 400);
    scoreboard.addScore("Alice", 500);
    scoreboard.addScore("Sam", 600);
    scoreboard.addScore("Tom", 700);
    scoreboard.addScore("Tim", 800);
    scoreboard.addScore("Cindy", 900);
    scoreboard.addScore("Lily", 1000);
    scoreboard.addScore("Linda", 1100);
    scoreboard.addScore("Linda", 1200);
    scoreboard.printScoreboard();
    return 0;
}