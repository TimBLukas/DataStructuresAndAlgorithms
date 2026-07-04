# Hashtables

## Hash funtions

A hash function is a function were you put in a string (any kind of data - a sequence of bytes) and get back a number.
A hash function basically maps maps strings to numbers. A hash function has the following requirements:
1. It needs to be consistent. If you put in "apple" and get back 3. Every time you put in "apple" you should get back 3. Without this hash tables won't work.
2. It should map different data to different numbers. For example, a hash function wouldn't fulfill its purpose if it always returns 1 for any word that is put in. In the best case, every different word should map to a different number.

This can be used to find the position in an array for the string that is inputed.
If the hashfunction receives "banana" as input and maps it to 3, you store banana at index 3 of the array.
This works because:
- The hash function consistently maps a name to the same index. Every time you put in a string, you'll get the same number back. So you can use it the first time to find were to store the value for the provided string. You can then use the string to find the value stored for it.
- The hash function maps different strings to different indexes. Everything maps to different slots in the array were you can store the value that should be associated to the key (string provided to the hash function).
- The hash function knows how big the array is and only returns valid indizes. If the array has five items, the hash function does not return 100 which would be an invalid index.

## Hashtables
In python Hashtables are called dictionaries and can be implemented like this:
```python
book = {}

book["apple"] = 0.67
book["banana"] = 1.3

print(book["banana"])
```

The string in the brackets is the value handed to the hash function and will serve as the key.
The value behind the equal sign is called "value" and is what is stored in the array at the index in the array that is returned by the hash function.

Uses cases of Hashtables:
- Every phone has a phonebook built in. Each name has a phone number associated with it.
- Hash tables are also used on a much larger scale: for example to resolve urls to actual IP adresses. For any website you go to, the address has to be translated to an IP adress, this process is called DNS resolution.
- Caching: If you make a request to a server, you will receive a web page. If you save the responnse you need to provide, you get the page a lot faster because the server does not have to complete as much work. The cache works by associating the url (facbook.com/about) and the data returned by the server for this address. The key (string for the hash function) is the url.

## Collisions

In reality hash functions don't always map a string to a distinct value, they can return the same number for different strings. This is called a collision.
There are many different ways to deal with collisions, the simplest one is: If multiple keys map to the same slot, start a linked list at that slot.
The search will be slower because once you are at the right index, you will have to search through the linked list to find the value you are searching for.

Key lessons:
- Hash functions are very important: If a hash function maps everything the the same key or produces many collisions it is not very useful.
- If the linked lists in the array get long, it slows down the hash table a lot. But they won't get to long if the hash function is good.

## Performance

Hash tables have O(1) time to look up but also to search and insert.
This means they take the same amount of time no matter the amount of elements. This means in the best case they are really fast, but in the worst case they are slow at all operations.
This means it is important that you need to avoid the worst case, which you can do by avoiding collisions.
To avoid collisions you need:
- A low load factor
- A good hash function

### Load factor

The load factor of a hash function is easy to calculate.
Hash tables use an array for storage, so you count the number of occupied slots in an array.
The load factor therefor measures how full the hash table is.
Having a load factor greater than one means you have more items than slots in your array. Once the load factor starts got grow, you need to add more slots to your hash table, which is named resizing.

Resizing is expensive and you don't want to resize to often, but avaraged out, hash tables take O(1) even with resizing.

### A good hash function

A good hash function distributes values in the array evenly.
A bad hash function groups values together and produces a lot of collisions.

> Note: There are many people who spend a lot of time on hash functions to figure out how to create the perfect one.
> One example would be CityHash (Google's Abseil library).



