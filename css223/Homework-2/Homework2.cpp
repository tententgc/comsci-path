#include <iostream> 
#include <string> 
#include <vector> 

using namespace std; 

//creted linked list for create polynomial
struct Node{
    int coeff; 
    int exp; 
    Node *next; 
    Node *prev; 
}; 

class Polynomial{
    private:
        Node *head; 
        Node *tail; 
    public: 
        Polynomial(){
            head = NULL; 
            tail = NULL; 
        }
        void insert(int coeff, int exp){
            Node *temp = new Node; 
            temp->coeff = coeff; 
            temp->exp = exp; 
            temp->next = NULL; 
            if(head == NULL){
                head = temp; 
                tail = temp; 
            }
            else{
                tail->next = temp; 
                tail = temp; 
            }
        }
        void print(){
            Node *temp = head; 
            while(temp != NULL){
                cout << temp->coeff << "x^" << temp->exp << " + "; 
                temp = temp->next; 
            }
            cout << endl; 
        }
        void add(Polynomial p2){
            Node *temp = head; 
            Node *temp2 = p2.head; 
            while(temp != NULL){
                while(temp2 != NULL){
                    if(temp->exp == temp2->exp){
                        temp->coeff = temp->coeff + temp2->coeff; 
                    }
                    temp2 = temp2->next; 
                }
                temp = temp->next; 
                temp2 = p2.head; 
            }
            temp = head; 
            while(temp != NULL){
                if(temp->coeff == 0){
                    if(temp == head){
                        head = temp->next; 
                    }
                    else if(temp == tail){
                        tail = temp->prev; 
                    }
                    else{
                        temp->prev->next = temp->next; 
                        temp->next->prev = temp->prev; 
                    }
                }
                temp = temp->next; 
            }
        }
        void multiply(Polynomial p2){
            Node *temp = head; 
            Node *temp2 = p2.head; 
            while(temp != NULL){
                while(temp2 != NULL){
                    temp->coeff = temp->coeff * temp2->coeff; 
                    temp->exp = temp->exp + temp2->exp; 
                    temp2 = temp2->next; 
                }
                temp = temp->next; 
                temp2 = p2.head; 
            }
        }
};



