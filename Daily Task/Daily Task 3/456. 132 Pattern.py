class Solution(object):
    def find132pattern(self, nums):
        second=float("-inf")
        l=len(nums)
        stack=[] 
        for i in range(l-1,-1,-1): 
            if nums[i]<second and second!=float("-inf"):
                return True
            while stack and stack[-1]<nums[i]: 
                second=stack.pop()
            stack.append(nums[i])
        return False
            
