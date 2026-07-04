# Hashtables

## Hash funtions

A hash function is a function were you put in a string (any kind of data - a sequence of bytes) and get back a number.
A hash function basically maps maps strings to numbers. A hash function has the following requirements:
1. It needs to be consistent. If you put in "apple" and get back 3. Every time you put in "apple" you should get back 3. Without this hash tables won't work.
2. It should map different data to different numbers. For example, a hash function wouldn't fulfill its purpose if it always returns 1 for any word that is put in. In the best case, every different word should map to a different number.


