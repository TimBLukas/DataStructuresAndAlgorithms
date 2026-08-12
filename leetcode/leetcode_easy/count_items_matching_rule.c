/**
* Leetcode 1773: COunt Items matching a rule
*
* You are given an array items, where each items[i] = [typei, colori, namei]
describes the type, color, and name of the ith item. You are also given a rule
represented by two strings, ruleKey and ruleValue.

* The ith item is said to match the rule if one of the following is true:
* - ruleKey == "type" and ruleValue == typei.
* - ruleKey == "color" and ruleValue == colori.
* - ruleKey == "name" and ruleValue == namei.
*
Return the number of items that match the given rule.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int countMatches(char ***items, int itemsSize, int *itemsColSize, char *ruleKey,
                 char *ruleValue) {
    int matching_cnt = 0;
    for (int i = 0; i < itemsSize; i++) {
        if (strcmp(ruleKey, "type") == 0 && strcmp(items[i][0], ruleValue) == 0)
            matching_cnt++;
        else if (strcmp(ruleKey, "color") == 0 &&
                 strcmp(items[i][1], ruleValue) == 0)
            matching_cnt++;
        else if (strcmp(ruleKey, "name") == 0 &&
                 strcmp(items[i][2], ruleValue) == 0)
            matching_cnt++;
    }
    return matching_cnt;
}
