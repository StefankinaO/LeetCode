class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        answer.insert(0, nums[0])
        for i in range(1, len(nums)):
            answer.insert(i, sum(nums[:i + 1]))
        return answer
