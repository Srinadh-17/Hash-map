class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
              
        myDict={}
        
        for i in range(len(nums)):
            
            if nums[i] in myDict and abs(i-myDict[nums[i]])<=k:
                return True
            myDict[nums[i]]=i
        return False
        