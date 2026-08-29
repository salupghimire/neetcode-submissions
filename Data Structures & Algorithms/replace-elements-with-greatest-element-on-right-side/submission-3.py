class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum=-1
        i=0
        a=len(arr)
        for x in range(a-1,-1,-1):
            current=arr[x]
            arr[x]=maximum
            maximum=max(maximum,current)
        return arr
                
                
