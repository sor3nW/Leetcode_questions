#solution for leetcode questionn 125 valid palindrome
#difficulty - easy

new = ""
for i in s:
    if i.isalnum():
        new += i.lower()
return new == new[::-1]

