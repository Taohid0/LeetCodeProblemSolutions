class Solution:
    def searchInsert(self,nums,target):
        index =0
        while index<len(nums) and nums[index]<target:
            index = index+1
        return index