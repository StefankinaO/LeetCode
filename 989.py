class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        number = ''
        ans = []
        for i in range(len(A)):
            number += str(A[i])
        number = str(int(number) + K)
        for i in range(len(number)):
            ans.append(number[i])
        return ans