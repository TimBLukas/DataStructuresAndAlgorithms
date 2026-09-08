/**
 * Leetcode 19: Remove Nth Node From End of List
 * Given the head of a linked list, remove the nth node from the end of the list
 * and return its head.
 */

#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *removeNthFromEnd(struct ListNode *head, int n) {
    struct ListNode *curr = head;

    int length = 0;
    while (curr != NULL) {
        curr = curr->next;
        length++;
    }
    curr = head;

    // safe guards
    if (length == 1) {
        return NULL;
    } else if (length == n) {
        return head->next;
    }

    int cnt = 0;
    struct ListNode *prev = malloc(sizeof(struct ListNode));
    while (cnt != length - n) {
        prev = curr;
        curr = curr->next;
        cnt++;
    }
    curr = prev;
    if (curr->next->next == NULL) {
        curr->next = NULL;
    } else {
        curr->next = curr->next->next;
    }

    return head;
}
