## Problem1 (https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
'''This code will give TLE for larger list, hence try to solve without using extra space
        numSet = set()
        for num in nums:
            numSet.add(num)

        res = []
        for i in range(1, len(nums)+1):
            if i not in numSet:
                res.append(i)
        return res'''
class Solution:
    def findDisappearedNumbers(self, nums):
        total = 0
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1) 

        return res
         
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(nums)) 
        
       
        