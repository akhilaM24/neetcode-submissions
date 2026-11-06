class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = right - left
            width = min(heights[left], heights[right])
            curr_area = height * width
            max_area = max(curr_area, max_area)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_area
        