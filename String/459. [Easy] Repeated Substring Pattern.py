# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        twice = f'{s}{s}'
        
        for i in range(1, n):
            if s == twice[i:i+n]:
                return True
            
        return False


# String - String Matching