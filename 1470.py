class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        b = nums[n:]
        nums1 = nums[:n]
        ans = []
        z, k = 0, 0
        for i in range(2 * n):
            if i % 2 == 0:
                ans.insert(i, nums1[z])
                z+= 1
            else:
                ans.insert(i, b[k])
                k+= 1
        return ans
