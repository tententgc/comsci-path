#include <stdio.h>
#include <stdlib.h>



#define MAXV 6 /* maximum number of vertices */

/*Structure for Vertex*/
struct node
{
    int label;         /*data*/
    char *name;        /*data*/
    struct node *next; /*Pointer to next node*/
};

struct node vertices[MAXV];
char *names[MAXV];

void addToList(struct node *x, int data);
void traverseGraph();
void initNames();
void displayNames();

int main()
{
    /*Initialize Names*/
    initNames();
    displayNames();

    /*Initialize the Array*/
    for (int i = 0; i < MAXV; i++)
    {
        vertices[i].label = i;
        vertices[i].name = names[i];
        vertices[i].next = NULL;
    }
    /*
        Say we have the following Edges {(0,1), (0,2), (1,2)}
        Let's build the Adjacency List.
    */

    addToList(&vertices[0], 1);
    addToList(&vertices[0], 3);
    addToList(&vertices[1], 2);
    addToList(&vertices[1], 0);
    addToList(&vertices[1], 4);
    addToList(&vertices[2], 1);
    addToList(&vertices[3], 0);
    addToList(&vertices[3], 5);
    addToList(&vertices[4], 1);
    

    /*Traverse the Adjacency List*/
    traverseGraph();

    return 0;
}

/*Here we are trying to add an edge x->y*/
void addToList(struct node *x, int data)
{
    printf("Going to Add %d to the Vertex %d \n", data, x->label);
    struct node *y = (struct node *)(malloc(sizeof(struct node)));
    if (y != NULL)
    {
        y->label = data;
        y->name = names[data];
        if (x->next != NULL)
            y->next = x->next;
        else
            y->next = NULL;

        x->next = y;
    }
}


void traverseGraph()
{
    // printf("Ready to traverse the graph \n");
    int array_size = sizeof(vertices) / sizeof(vertices[0]);
    // printf("No of elements in Array = %d \n", array_size);
    printf("\n");
    printf("Let's see who all are Friends \n");
    printf("\n");
    for (int i = 0; i < MAXV; i++)
    {
        struct node *temp = &vertices[i];
        printf("%s is friend to --> ", temp->name);
        if (temp->next != NULL)
        {
            temp = temp->next;
            while (temp != NULL)
            {
                printf("%s", temp->name);
                if (temp->next != NULL)
                    printf(", ");
                temp = temp->next;
            }
        }
        printf("\n\n---------------------------------------------\n\n");
    }
}

void initNames()
{
    names[0] = "Ankur";
    names[1] = "Dikshit";
    names[2] = "Mohan";
    names[3] = "Nidhi";
    names[4] = "Reena";
    names[5] = "Suresh";
}

void displayNames()
{
    printf("\nWe have the following folks staying in a small town \n\n");
    for (int i = 0; i < MAXV; i++)
    {
        printf("%s ", names[i]);
    }
    printf("\n\n---------------------------------------------\n\n");
}