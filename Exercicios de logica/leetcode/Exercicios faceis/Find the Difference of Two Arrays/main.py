class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set([n for n in nums1 if n not in nums2])), list(set([n for n in nums2 if n not in nums1]))]
