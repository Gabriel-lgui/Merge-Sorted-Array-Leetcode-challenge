class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums2) > 0:
            n = len(nums2)
        else:
            n = 0
        
        if nums1[0] == 0:
            m = 0
            c = nums2[0]
            nums1.remove(0)
            nums1.insert(0, c)
        else:
            m = len(nums1) - n
            a = m
            b = len(nums2)
            c = len(nums1)
            while b > 0:
                if nums1[c-1] == 0 and nums1[c-2] == 0:
                    nums1.remove(nums1[c-1])
                    nums1.insert(c-1, nums2[b-1])
                    b -= 1
                    c -= 1
                elif nums1[c-1] == 0 and nums1[c-2] > nums2[b-1]:
                    nums1.remove(nums1[c-1])
                    nums1.insert(c-1, nums1[c-2])
                    a -= 1
                    c -= 1
                elif nums1[c-1] <= nums2[b-1]:
                    nums1.remove(nums1[c-1])
                    nums1.insert(c-1, nums1[a-1])
                    a -= 1
                    c -= 1
                else:
                    nums1.remove(nums1[c-1])
                    nums1.insert(c-1, nums2[b-1])
                    b -= 1
                    c -= 1