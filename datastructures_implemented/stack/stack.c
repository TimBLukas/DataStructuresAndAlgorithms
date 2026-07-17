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
} Stack;

Stack* stack_create()
{
    Stack *stack = malloc(sizeof(Stack));

    stack->q1 = malloc(sizeof(Queue));
    stack->q2 = malloc(sizeof(Queue));

    queue_initialize(stack->q1);
    queue_initialize(stack->q2);

    return stack;
}

void stack_push(Stack* obj, int x)
{
    queue_push(obj->q2, x);

    while (!queue_isEmpty(obj->q1))
        queue_push(obj->q2, queue_pop(obj->q1));

    Queue *tmp = obj->q1;
    obj->q1 = obj->q2;
    obj->q2 = tmp;
}

int stack_pop(Stack* obj)
{
    return queue_pop(obj->q1);
}

int stack_top(Stack* obj)
{
    return queue_peek(obj->q1);
}

bool stack_is_empty(Stack* obj)
{
    return queue_isEmpty(obj->q1);
}

void stack_free(Stack* obj)
{
    free(obj->q1);
    free(obj->q2);
    free(obj);
}