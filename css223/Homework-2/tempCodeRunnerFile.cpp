        Polynomial result;
        Node *temp1 = head;
        Node *temp2 = p.head;
        while (temp1 != NULL) {
            while (temp2 != NULL) {
                result.add(temp1->coefficient * temp2->coefficient, temp1->exponent + temp2->exponent);
                temp2 = temp2->next;
            }
            temp1 = temp1->next;
            temp2 = p.head;
        }
        return result;