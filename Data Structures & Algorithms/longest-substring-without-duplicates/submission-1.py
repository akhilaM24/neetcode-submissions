class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        valid_window = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in valid_window:
                valid_window.remove(s[left])
                left+=1
            valid_window.add(s[right])
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)

        return max_len


        