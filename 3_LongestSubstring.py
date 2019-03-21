class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)-1):
                if s[j+1] not in s[i:j]:
                    print(s[i:j])
        
Solution.lengthOfLongestSubstring(Solution, 'abcabc')