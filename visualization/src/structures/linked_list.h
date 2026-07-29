#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct ListNode
{
        int value;
        struct ListNode* next;
} ListNode;

typedef struct
{
        ListNode* head;
        int size;
} LinkedList;


// Node Functions
ListNode* listnode_create(int val);

void listnode_destroy(ListNode* node);

void listnode_print(ListNode* node);

ListNode* listnode_get_next(const ListNode* node);

void listnode_set_next(ListNode* node, ListNode* next);


// Linked List Functions

LinkedList* linkedlist_create(void);

void linkedlist_insert_front(LinkedList* list, int val);

void linkedlist_insert_back(LinkedList* list, int val);

void linkedlist_remove(LinkedList* list, int val);

void linkedlist_print(const LinkedList* list);

void linkedlist_destroy(LinkedList* list);

ListNode* linkedlist_find(LinkedList* list, int val);

int linkedlist_size(const LinkedList* list);

void linkedlist_clear(LinkedList* list);

void linkedlist_reverse(LinkedList* list);

#endif
