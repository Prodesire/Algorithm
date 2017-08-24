#include<iostream>


typedef struct tagSNode
{
    int value;
    tagSNode* pNext;
    tagSNode(int v) : value(v), pNext(nullptr) {}
}SNode;


SNode* Add(SNode* pHead1, SNode* pHead2)
{
    SNode* pSum = new SNode(0);
    SNode* pTail = pSum;
    SNode* p1 = pHead1->pNext;
    SNode* p2 = pHead1->pNext;
    int carry = 0;
    int value;
    
    while (p1 && p2)
    {
        value = p1->value + p2->value + carry;
        carry = value / 10;
        value = value % 10;
        pTail->pNext = new SNode(value);
        pTail = pTail->pNext;

        p1 = p1->pNext;
        p2 = p2->pNext;
    }

    SNode* p = p1 ? p1 : p2;
    while (p) 
    {
        value = p->value + carry;
        carry = value / 10;
        value = value % 10;
        pTail->pNext = new SNode(value);
        pTail = pTail->pNext;
    }

    if (carry != 0)
        pTail->pNext = new SNode(carry);
    return pSum;
}


int _tmain(int argc, wchar_t* argv[])
{
    SNode* pHead1 = new SNode(0);
    int i;
    for (i = 0; i < 6; i++)
    {
        SNode* p = new SNode(rand() % 10);
        p->pNext = pHead1->pNext;
        pHead1->pNext = p;
    }

    SNode* pHead2 = new SNode(0);
    int i;
    for (i = 0; i < 9; i++)
    {
        SNode* p = new SNode(rand() % 10);
        p->pNext = pHead2->pNext;
        pHead2->pNext = p;
    }
}
