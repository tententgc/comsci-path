#include <iostream> 
#include <string> 

using namespace std; 

// create scoreboard top 10 with doubly linked list 
// when add newscore to scoreboard, it will be added to the right position 
// and the lowest score will be removed 
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
            temp->next = current; 
            temp->prev = current->prev; 
            current->prev->next = temp; 
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
    Scoreboard s; 
    s.addScore("A", 100);
    s.addScore("B", 200);
    s.addScore("C", 300);
    s.addScore("D", 400);
    s.addScore("E", 500);
    s.addScore("F", 600);
    s.addScore("G", 700);
    s.addScore("H", 800);
    s.addScore("I", 900);
    s.addScore("J", 1000);
    s.addScore("K", 1100);
    s.addScore("L", 1200);
    s.addScore("M", 1300);
    s.addScore("N", 1400);

    s.printScoreboard();
}