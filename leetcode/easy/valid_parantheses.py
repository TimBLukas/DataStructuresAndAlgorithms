class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"(": ")", "[": "]", "{": "}"}
        current_brackets = []
        for c in s:
            if c in bracket_pairs:
                current_brackets.append(c)
            else:
                if len(current_brackets) > 0 and bracket_pairs.get(current_brackets[-1]) == c:
                   current_brackets.pop() 
                else:
                    return False
        if len(current_brackets) == 0:
            return True
        return False
