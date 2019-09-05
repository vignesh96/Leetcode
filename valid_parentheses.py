class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = True
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif s[i] in ")}]":
                if not stack:
                    flag = False
                elif (stack[-1] == "(" and s[i] == ")") or (s[i] == "]" and stack[-1] == "[") or (s[i] == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    flag = False
            if flag == False:
                break
        
        return True if flag and not stack else False
            
