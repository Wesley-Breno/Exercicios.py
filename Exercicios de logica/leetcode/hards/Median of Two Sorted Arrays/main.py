import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return np.median(sorted(nums1 + nums2))