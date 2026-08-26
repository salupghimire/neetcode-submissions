class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        max_a = 0
        for num in nums:
            if num == 1:
                a += 1
            else:
                if a > max_a: max_a = a
                a = 0
        if a > max_a: max_a = a
        return max_a