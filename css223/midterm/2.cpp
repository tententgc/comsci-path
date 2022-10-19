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

// Big O: O(n)
// enqueue: O(1) => เท่าเดิมทั้ง 2 อันเลยยย
// dequeue: O(n) => ต้อง pop ทั้ง stack ออกมาเก็บไว้ในตัวแปรเพื่อเอาค่าตัวแรกออกมา แล้ว push กลับไปทีละตัว จึงเป็น O(n)
// ในเคสนี้เลยใช้ stack กับ queue แล้วเท่ากัน
