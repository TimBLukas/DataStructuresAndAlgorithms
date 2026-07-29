# include "linked_list.h"

#include <stdlib.h>
#include <stdio.h>


/**
* List Node functions
*/
ListNode* listnode_create(int val) 
{
        ListNode* node = malloc(sizeof(ListNode));
        if ( node == NULL )
                return NULL;

        node->value = val;
        node->next = NULL;

        return node;
}

void listnode_destroy(ListNode* node) {
        ListNode* curr = node;
        ListNode* next;
        while ( curr != NULL ) {
                next = curr->next;
                free(curr);
                curr = next;
        }
}

void listnode_print(ListNode* node)
{
        ListNode* curr = node;
        while ( curr != NULL ) {
                printf("%d", curr->value);
                if ( curr->next != NULL )
                        printf(" -> ");
                curr = curr->next;
        }
        printf("\n");
}

ListNode* listnode_get_next(const ListNode* node)
{
        return node->next;
}

void listnode_set_next(ListNode* node, ListNode* next)
{
        node->next = next;
}

/**
* Linked List functions
*/
LinkedList* linkedlist_create()
{
        LinkedList* list = malloc(sizeof(LinkedList));
        if ( list == NULL )
                return NULL;

        list->size = 0;
        list->head = NULL;

        return list;
}

void linkedlist_insert_front(LinkedList* list, int val) 
{
        ListNode* new_node =listnode_create(val);
        new_node->next = list->head;

        list->head = new_node;
        list->size++;
}

void linkedlist_insert_back(LinkedList* list, int val)
{
        ListNode* new_node = listnode_create(val);

        if ( list->head == NULL ) {
                list->head = new_node;
                list->size++;
                return;
        }

        ListNode* curr = list->head;
        while ( curr->next != NULL )
                curr = curr->next;

        listnode_set_next(curr, new_node);
        list->size++;
}

// Removes first occurence of the provided value
void linkedlist_remove(LinkedList* list, int val)
{
        if ( list->head == NULL)
                return;

        ListNode* curr = list->head;
        if ( curr->value == val ) {
                list->head = ( curr->next == NULL ) ? NULL : curr->next;
                free(curr);
                list->size--;
                return;
        }

        ListNode* prev = list->head;
        while ( curr != NULL ) {
                if ( curr->value == val ) {
                        prev->next = curr->next;
                        free(curr);
                        list->size--;
                        return;
                } else {
                        prev = curr;
                        curr = curr->next;
                }
        }
}

void linkedlist_print(const LinkedList* list)
{
        listnode_print(list->head);
}

void linkedlist_destroy(LinkedList* list)
{
        listnode_destroy(list->head);
        list->head = NULL;
        list->size = 0;

        free(list);
}

ListNode* linkedlist_find(LinkedList* list, int val)
{
        ListNode* curr = list->head;
        while ( curr != NULL ) {
                if ( curr->value == val ) {
                        return curr;
                } 
                curr = curr->next;
        }
        return NULL;
}

int linkedlist_size(const LinkedList* list)
{
        return list->size;
}

void linkedlist_clear(LinkedList* list)
{
        listnode_destroy(list->head);

        list->size = 0;
        list->head = NULL;
}

void linkedlist_reverse(LinkedList* list)
{
        if ( list->head == NULL )
                return;

        if ( list->head->next == NULL )
                return;
        ListNode* next = list->head->next;
        ListNode* curr = list->head;
        ListNode* prev = NULL;

        while ( next != NULL ) {
                curr->next = prev;
                prev = curr;
                curr = next;
                next = next->next;
        }

        curr->next = prev;
        list->head = curr;
}


