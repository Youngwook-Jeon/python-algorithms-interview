import collections
import re

# leetcode 125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


sol = Solution()
print(sol.isPalindrome("A man, a plan a canal: Panama"))