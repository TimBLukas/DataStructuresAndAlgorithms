#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

const int BUCKETS = 64;


typedef struct 
{
        char* key;
        int value;
} Value;


typedef struct Node
{
        Value val;
        struct Node* next;
} Node;


typedef struct 
{
        Node hash_table[BUCKETS];
} HashTable;

HashTable hashtable_create(void);
void hashtable_add( char* key, int value );
int hashtable_get( char* key );
int hash( char* input );
int get_idx( char* input );
void extend_linked_list( Node* head ); 


int main() 
{
        return 0;
}

HashTable hashtable_create()
{
        HashTable hash_table;
        for (int i=0; i < BUCKETS; i++)
        {
                hash_table.hash_table[i].val = NULL;
                hash_table.hash_table[i].next = NULL;
        }
        return hash_table;
}

void hashtable_add(HashTable* hash_table, char* key, int value)
{
    int idx = get_idx(key);

    if (hash_table->hash_table[idx].val == NULL)
    {
        hash_table->hash_table[idx].val = malloc(sizeof(Value));

        hash_table->hash_table[idx].val->key = key;
        hash_table->hash_table[idx].val->value = value;
        hash_table->hash_table[idx].next = NULL;
    }
    else
    {

    }
}

int hashtable_get( char* key );

int hash( char* input )
{
        return strlen(input) % BUCKETS;
}

int get_idx( char* input )
{
        return hash( input );
}

void extend_linked_list( Node* head, char* key, int val )
{
        Node* curr = head;

        while ( curr->next != NULL )
        {
                curr = curr->next;
        }

        Value v = { key, val };
        Node n = { v, NULL };
        curr->next = &n;
}