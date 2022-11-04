#solution for leetcode question 20 Valid Parenthesis
#difficulty - easy

stack = []
pairs = { ")": "(" , "}":"{" , "]": "["}
for i in s:
    if i in pairs:
        if stack and stack[-1] == pairs[i]:
            stack.pop()
        else:
            return False
    else:
        stack.append(i)
return True if not stack else False
