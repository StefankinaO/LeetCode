class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        maxim = 0
        for i in range(1, len(arr)):
            maxim = max(arr[i:])
            if maxim < arr[i]:
                ans.append(arr[i])
                maxim = arr[i]
            else:
                ans.append(maxim)
        ans.append(-1)
        return (ans)           