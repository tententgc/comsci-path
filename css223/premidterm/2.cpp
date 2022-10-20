#include <iostream>
#include <stack>

using namespace std;
class Queue
{
private:
    stack<int> s;

public:
    void enque(int x)
    {
        s.push(x);
    }
    int deque()
    {
        if (s.empty())
        {
            cout << "Queue is empty";
            exit(0);
        }
        int x = s.top();
        s.pop();
        if (s.empty())
        {
            return x;
        }
        int item = deque();
        s.push(x);
        return item;
    }
};


int main()
{
    Queue q;
    q.enque(1);
    q.enque(2);
    q.enque(3);
    cout << "Output: " << q.deque() << "\n";
    cout << "Output: " << q.deque() << "\n";
    cout << "Output: " << q.deque() << "\n";
    cout << "Output: " << q.deque() << "\n";
    return 0;
}