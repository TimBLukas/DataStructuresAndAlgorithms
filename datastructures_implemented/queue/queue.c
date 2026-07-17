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