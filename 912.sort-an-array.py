#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (56.48%)
# Likes:    6859
# Dislikes: 829
# Total Accepted:    944.4K
# Total Submissions: 1.7M
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order and return
# it.
# 
# You must solve the problem without using any built-in functions in O(nlog(n))
# time complexity and with the smallest space complexity possible.
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not
# changed (for example, 2 and 3), while the positions of other numbers are
# changed (for example, 1 and 5).
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def mergeSort(self, left_array: list, right_array: list, orig_array: list) -> None:
        left_length = len(left_array)
        right_length = len(right_array)
        orig, left, right = 0, 0, 0

        while (left < left_length and right < right_length):
            if left_array[left] < right_array[right]:
                orig_array[orig] = left_array[left]
                left += 1
            else:
                orig_array[orig] = right_array[right]
                right += 1

            orig += 1
        
        while (left < left_length):
            orig_array[orig] = left_array[left]
            orig += 1
            left += 1
        
        while (right < right_length):
            orig_array[orig] = right_array[right]
            orig += 1
            right += 1

    def sortArray(self, nums: list[int]):
        #### QUICK SORT #### (can be better with picking a better pivot)     AVERAGE CASE: O(n logn)   WORST CASE: O(n^2)
                # nums_len = len(nums)
                # if nums_len <= 1:
                #     return nums
                
                # left_pointer = -1
                # pointer = nums[nums_len - 1]

                # for i in range(nums_len):
                #     if i == nums_len - 1:
                #         left_pointer += 1
                #         nums[i], nums[left_pointer] = nums[left_pointer], nums[i]
                #     elif nums[i] <= pointer:
                #         left_pointer += 1
                #         nums[i], nums[left_pointer] = nums[left_pointer], nums[i] 
                
                # return self.sortArray(nums[:left_pointer]) + self.sortArray(nums[left_pointer:])
            
        #### MERGE SORT #### AVERAGE/WORST CASE: O(n logn)
        if len(nums) <= 1: 
            return nums
        nums_split = len(nums) // 2
        left_array = nums[:nums_split]
        right_array  = nums[nums_split:]
        
        self.sortArray(left_array)
        self.sortArray(right_array)
        self.mergeSort(left_array, right_array, nums)

        return nums
# @lc code=end
import random
solution = Solution()
nums = list(range(1, 15001))
random.shuffle(nums)

# nums = list(range(1, 16))
# random.shuffle(nums)

print(solution.sortArray(nums))
