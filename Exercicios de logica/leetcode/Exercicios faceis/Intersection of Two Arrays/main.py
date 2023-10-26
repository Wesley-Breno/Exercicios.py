class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set([n for n in nums1 if n in nums2]))
