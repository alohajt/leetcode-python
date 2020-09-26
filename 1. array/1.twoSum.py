class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            newlist=nums[i+1:]
            num2=target-nums[i]
            if num2 in newlist:
                return [i,newlist.index(num2)+i+1]