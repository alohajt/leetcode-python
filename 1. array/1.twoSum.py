# nums = [2, 7, 11, 15]
# target = 9


# def twoSum(self, nums, target):
#     for i in range(len(nums)):
#         print("i is", i)
#         newlist = nums[i+1:]
#         num2 = target-nums[i]
#         if num2 in newlist:
#             print([i, newlist.index(num2) + i + 1])
#             return [i, newlist.index(num2) + i + 1]


# twoSum(twoSum, nums, target)

class Solution:
    def twoSum(self, nums, target):
        pos = dict()
        for i, num in enumerate(nums):
            if target - num in pos:
                return [pos[target - num], i]
            else:
                pos[num] = i
        return [0, 0]