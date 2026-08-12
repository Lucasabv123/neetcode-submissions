class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        d = []
        for n in nums:
            if n in s:
                d.append(n)
                return True 
            else:
                s.add(n)
        return False
        
                


            
        

        
        