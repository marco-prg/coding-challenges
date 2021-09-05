# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # return list(collections.Counter(t) - collections.Counter(s))[0]
        
        result = 0
        
        for c in s+t:
            # The ord() function returns an integer representing the Unicode character.
            result ^= ord(c)
        
        # The chr() method returns a character (a string) from an integer 
        # (represents unicode code point of the character).
        return chr(result)