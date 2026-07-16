/**
 * Leetcode 225: Implement Stack using Queues
 *
 * Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
 * 
 * Implement the MyStack class:
 *
 * void push(int x) Pushes element x to the top of the stack.
 * int pop() Removes the element on the top of the stack and returns it.
 * int top() Returns the element on the top of the stack.
 * boolean empty() Returns true if the stack is empty, false otherwise.
 * Notes:
 *
 * You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
 * Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 */

#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int items[MAX_SIZE];
    int front;
    int rear;
} Queue;

void queue_initialize(Queue *q)
{
    q->front = 0;
    q->rear = 0;
}

bool queue_isEmpty(Queue *q)
{
    return q->front == q->rear;
}

bool queue_isFull(Queue *q)
{
    return q->rear == MAX_SIZE;
}

void queue_push(Queue *q, int value)
{
    if (queue_isFull(q))
        return;

    q->items[q->rear++] = value;
}

int queue_pop(Queue *q)
{
    if (queue_isEmpty(q))
        return -1;

    return q->items[q->front++];
}

int queue_peek(Queue *q)
{
    if (queue_isEmpty(q))
        return -1;

    return q->items[q->front];
}

typedef struct {
    Queue *q1;
    Queue *q2;
} MyStack;

MyStack* myStackCreate()
{
    MyStack *stack = malloc(sizeof(MyStack));

    stack->q1 = malloc(sizeof(Queue));
    stack->q2 = malloc(sizeof(Queue));

    queue_initialize(stack->q1);
    queue_initialize(stack->q2);

    return stack;
}

void myStackPush(MyStack* obj, int x)
{
    queue_push(obj->q2, x);

    while (!queue_isEmpty(obj->q1))
        queue_push(obj->q2, queue_pop(obj->q1));

    Queue *tmp = obj->q1;
    obj->q1 = obj->q2;
    obj->q2 = tmp;
}

int myStackPop(MyStack* obj)
{
    return queue_pop(obj->q1);
}

int myStackTop(MyStack* obj)
{
    return queue_peek(obj->q1);
}

bool myStackEmpty(MyStack* obj)
{
    return queue_isEmpty(obj->q1);
}

void myStackFree(MyStack* obj)
{
    free(obj->q1);
    free(obj->q2);
    free(obj);
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/
