class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        first_val, val = 0, 0
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    val += 1
            ans.append(val)
            val = 0
        return ans
