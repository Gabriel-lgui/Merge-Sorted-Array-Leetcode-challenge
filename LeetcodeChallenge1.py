class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if nums2[1] == 0:
            n = 0
        else:
            n = len(nums2)
        
        if nums1[1] == 0:
            m = 0
        else:
            m = len(nums1) + n
            
        
            