class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_list = [1]
        right_list = [1]
        l, r = 1, 1
        answer = [0] * len ( nums )
        for i in range ( 1, len ( nums ) ):
            l *= nums[i - 1]
            left_list.append ( l )

        for i in range ( len ( nums ) - 2, -1, -1 ):
            r *= nums[i + 1]
            right_list.append ( r )
        right_list = right_list[::-1]

        for i in range ( len ( left_list ) ):
            answer[i] = left_list[i] * right_list[i]
        return answer
























