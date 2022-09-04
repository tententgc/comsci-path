#include <iostream> 
#include <string>
using namespace std;

//create scoreboard top10 with doubly linked list if the score is higher than the lowest score in the top10 list delete the lowest score and add the new score
//create a function to print the top10 list
//create a function to check if the score is higher than the lowest score in the top10 list
//create a function to delete the lowest score in the top10 list
//create a function to add the new score to the top10 list

class Score
{
public:
	Score(string n, int s);
	string name;
	int score;
	Score *next;
	Score *prev;
};

Score::Score(string n, int s)
{
	name = n;
	score = s;
	next = NULL;
	prev = NULL;
}

class ScoreBoard
{
public:
	ScoreBoard();
	~ScoreBoard();
	void print();
	bool checkScore(int s);
	void addScore(string n, int s);
private:
	Score *head;
	Score *tail;
};

ScoreBoard::ScoreBoard()
{
	head = NULL;
	tail = NULL;
}

ScoreBoard::~ScoreBoard()
{
	Score *current = head;
	while (current != NULL)
	{
		Score *temp = current;
		current = current->next;
		delete temp;
	}
}

void ScoreBoard::print()
{
	Score *current = head;
	while (current != NULL)
	{
		cout << current->name << ": " << current->score << endl;
		current = current->next;
	}
}

bool ScoreBoard::checkScore(int s)
{
	Score *current = head;
	if (s > current->score)
	{
		return true;
	}
	else
	{
		return false;
	}
}

void ScoreBoard::addScore(string n, int s)
{
	Score *newScore = new Score(n, s);
	if (head == NULL)
	{
		head = newScore;
		tail = newScore;
	}
	else
	{
		Score *current = head;
		while (current != NULL)
		{
			if (s > current->score)
			{
				newScore->next = current;
				current->prev = newScore;
				head = newScore;
				break;
			}
			else if (current->next == NULL)
			{
				current->next = newScore;
				newScore->prev = current;
				tail = newScore;
				break;
			}
			else if (s < current->score && s > current->next->score)
			{
				newScore->next = current->next;
                current->next->prev = newScore;
                current->next = newScore;
                newScore->prev = current;
                break;
            }
            current = current->next;
        }
    }
}

int main(){ 
    ScoreBoard *scoreboard = new ScoreBoard();
    scoreboard->addScore("John", 100);
    scoreboard->addScore("Mary", 200);
    scoreboard->addScore("Tom", 300);
    scoreboard->addScore("Bob", 400);
    scoreboard->addScore("Alice", 500);
    scoreboard->addScore("Peter", 600);
    scoreboard->addScore("Jack", 700);
    scoreboard->addScore("Lily", 800);
    scoreboard->addScore("Jane", 900);
    scoreboard->addScore("Mike", 1000);
    scoreboard->addScore("Tom", 790);
    scoreboard->print();
    cout << endl;

}