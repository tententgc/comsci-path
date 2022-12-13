#include <iostream>
using namespace std;

class Graph
{
    int v;
    int **adj;

public:
    Graph(int v);
    void addEdge(int start, int e);
    void printMatrix();
    void nonConnected(int start);
    void friendRecommend(int start);
};

Graph::Graph(int v)
{
    this-> v = v;
    adj = new int *[v];
    for (int row = 0; row < v; row++)
    {
        adj[row] = new int[v];
        for (int column = 0; column < v; column++)
        {
            adj[row][column] = 0;
        }
    }
}

// Add an edge to the graph
void Graph::addEdge(int i, int j)
{
    adj[i][j] = 1;
    adj[j][i] = 1;
}

// Print the Matrix
void Graph::printMatrix()
{
    for (int i = 0; i < v; i++)
    {
        cout << i << " : ";
        for (int j = 0; j < v; j++)
            cout << adj[i][j] << " ";
        cout << "\n";
    }
}

char friends(int n)
{
    if (n == 0)
    {
        return 'A';
    }
    else if (n == 1)
    {
        return 'B';
    }
    else if (n == 2)
    {
        return 'C';
    }
    else if (n == 3)
    {
        return 'D';
    }
    else if (n == 4)
    {
        return 'E';
    }
    else if (n == 5)
    {
        return 'F';
    }
    else if (n == 6)
    {
        return 'G';
    }
    else if (n == 7)
    {
        return 'H';
    }
    else
    {
        return 'I';
    }
}

void Graph::friendRecommend(int start)
{
    int max = 0;
    int maxIndex = 0;
    for (int i = 0; i < v; i++)
    {
        int count = 0;
        for (int j = 0; j < v; j++)
        {
            if (adj[start][j] == 1 && adj[i][j] == 1 && i != start && adj[i][start] == 0)
            {
                count++;
            }
        }
        if (count > max && i != start)
        {
            max = count;
            maxIndex = i;
        }
    }
    cout << friends(start) << " is recommend to " << friends(maxIndex);
    cout << endl;
}

int main()
{

    int v = 9;
    char arr[9] = {'A','B','C','D','E','F','G','H','I'};


    Graph G(v);

    // friends of A
    G.addEdge(0, 1);
    G.addEdge(0, 3);
    G.addEdge(0, 5);
    G.addEdge(0, 4);

    // friends of B
    G.addEdge(1, 0);
    G.addEdge(1, 3);
    G.addEdge(1, 4);
    G.addEdge(1, 8);

    // friends of C
    G.addEdge(2, 3);
    G.addEdge(2, 4);

    // friends of D
    G.addEdge(3, 0);
    G.addEdge(3, 1);
    G.addEdge(3, 2);
    G.addEdge(3, 5);

    // friends of E
    G.addEdge(4, 0);
    G.addEdge(4, 1);
    G.addEdge(4, 2);

    // friends of F
    G.addEdge(5, 0);
    G.addEdge(5, 3);
    G.addEdge(5, 6);

    // friends of G
    G.addEdge(6, 5);
    G.addEdge(6, 7);

    // friends of H
    G.addEdge(7, 0);
    G.addEdge(7, 6);
    G.addEdge(7, 8);

    // friends of I
    G.addEdge(8, 1);
    G.addEdge(8, 6);

    G.printMatrix();

    cout << endl;

    G.friendRecommend(0);
    G.friendRecommend(1);
    G.friendRecommend(2);
    G.friendRecommend(3);
    G.friendRecommend(4);
    G.friendRecommend(5);
    G.friendRecommend(6);
    G.friendRecommend(7);
    G.friendRecommend(8);

    cout << endl;

}