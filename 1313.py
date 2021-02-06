class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        if len(nums) > 2:
            n = len(nums) // 2
            for i in range(len(nums) - n):
                freg, val = nums[2*i], nums[2*i+1]
                z = 1
                while z <= freg:
                    ans.append(val)
                    z += 1
                z = 0
                
        else:
            freg, val = nums[0], nums[1]
            z = 1
            while z <= freg:
                ans.append(val)
                z += 1
            z = 0
        return ans
