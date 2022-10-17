#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(self, s, t):
        a = sorted(s)
        b = sorted(t)
        if a==b:
            return True
        else:
            return False
#sort the first list
#sort the second list
#if the lists are equal when they are sorted then t must be an anagram of s
#else, t is not an anagra of s
