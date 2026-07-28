#include <stdlib.h>


/**
* Definition of singly linked list
*/
struct ListNode {
        int val;
        struct ListNode *next;
};


/**
* Solution
*/

struct ListNode* removeElements(struct ListNode* head, int val)
{
        if (head == NULL)
                return head;

        struct ListNode dummy;
        dummy.next = head;

        struct ListNode* prev = &dummy;
        struct ListNode* curr = head;

        while ( curr != NULL ) {
                if ( curr->val == val ) {
                        prev->next = curr->next;
                        curr = curr->next;
                } else {
                        prev = prev->next;
                        curr = curr->next;
                }

        }

        return dummy.next;

}


/**
*
* Problem: given the head of a linked list and an integer `val` remove all the nodes of the linked list that has `Node.val == val`
* -> return head
*
*  e.g. 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6         and     val = 6
*  returns 1 -> 2 -> 3 -> 4 -> 5
*/
