class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1]>0:
                dp[i] = dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]
            max_val = max(max_val, dp[i])
        return max_val