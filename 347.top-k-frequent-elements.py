#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (64.71%)
# Likes:    18474
# Dislikes: 733
# Total Accepted:    2.9M
# Total Submissions: 4.6M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # candidates = {}

        # for num in nums:
        #     candidates[num] = candidates.get(num, 0) + 1
        
        
        # candidates = dict(sorted(candidates.items(), key=lambda item: item[1], reverse=True))

        # return list(candidates.keys())[:k]


        #### BUCKET SORT
        counter = {}
        nums_len = len(nums)
        buckets = [[] for _ in range(nums_len + 1)]
        top_k = []

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for num, count in counter.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k.append(num)

                if len(top_k) == k:
                    return top_k
        
        return top_k
# @lc code=end

solution = Solution()
print(solution.topKFrequent([1], 1))