/**
 * Leetcode 2181: Merge Nodes in Between Zeros
 *
 * You are given the head of a linked list, which contains a series of integers separated by 0's.
 * The beginning and end of the linked list will have Node.val == 0.
 *
 * For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes.
 * The modified list should not contain any 0's.
 *
 * Return the head of the modified linked list.
*/

#include <stdlib.h>
#include <stdio.h>

/**
 * Definition for singly-linked list.
 */

struct ListNode 
{
    int val;
    struct ListNode *next;
};


struct ListNode* mergeNodes(struct ListNode* head) 
{
        struct ListNode* curr = head;
        struct ListNode* tail = head->next;
        int count = 0;

        while ( tail != NULL )
        {
                if ( tail->val != 0 )
                {
                        count += tail->val;
                        tail = tail->next;
                }
                else
                {
                        curr->val = count;

                        tail = tail->next;
                        if ( tail != NULL)
                                curr = curr->next;
                        count = 0;
                }
                printf("%d, %d\n", count, curr->val);
        }
        curr->next = NULL;

        return head;
}
