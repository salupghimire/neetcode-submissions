class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i= 0
        maximum=0
        for num in nums:
            if num==1:
                i+=1
                maximum=max(maximum,i)
            else:
                i=0
        return maximum

      