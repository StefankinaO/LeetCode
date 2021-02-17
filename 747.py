class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxim = max(nums)
        nums1 = nums.copy()
        nums.remove(maxim)
        nums.append(maxim // 2)
        if max(nums) == maxim // 2:
            return nums1.index(maxim)
        else:
            return -1