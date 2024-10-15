class Solution:
    def maxArea(self, height: List[int]) -> int:
        capacity = float ( "-inf" )
        left, right = 0, len ( height ) - 1

        while left <= right:
            peak = min ( height[right], height[left] )
            breadth = right - left
            curCapacity = peak * breadth
            capacity = max ( capacity, curCapacity )

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return capacity