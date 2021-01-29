class Solution:
    def findLucky(self, arr: List[int]) -> int:
        answer = -1
        arr = sorted(arr)
        for i in range(len(arr)):
            print(arr[i], count(arr[i]))
            if arr.count(arr[i]) == arr[i]:
                answer = arr[i]
        return answer
