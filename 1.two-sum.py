#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_of_numbers = {}

        for index, num in enumerate(nums):
            pair = target - num
            
            if pair in hash_of_numbers:
                return [index, hash_of_numbers[pair]]
            else:
                hash_of_numbers[num] = index

        return []
# @lc code=end

solution = Solution()
print(solution.twoSum([3,2,4], target = 6))