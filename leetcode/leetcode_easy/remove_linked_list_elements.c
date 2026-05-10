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

        // 1. get node to use while iterating
        struct ListNode dummy;
        dummy.next = head;

        struct ListNode* prev = &dummy;
        struct ListNode* curr = head;

        // 2. iterate through list
        while (curr != NULL) 
        {
                // 3. Check condition
                if (curr->val == val)
                {
                        prev->next = curr->next;
                        // Only move curr pointer
                        curr = curr->next;
                }
                else 
                {
                        // move both pointers
                        prev = prev->next;
                        curr = curr->next;
                }

        }

        // 6. return head of linked list
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
