class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        mapping = {"[":"]", "{":"}", "(":")"}
        stack = []

        for p in s:
            if p in mapping:
                stack.append(p)
            else:
                if stack:
                    temp = stack.pop()
                    if mapping[temp] == p:
                        continue
                return False
        
        return not stack