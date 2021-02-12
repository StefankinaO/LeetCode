class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_arr = 0
        print(sum_arr)
        if len(arr) !=0:
            for i in range(len(arr)):
                sum_arr += arr[i]
                for j in range(i + 2, len(arr)):
                    if len(arr[i:j + 1]) % 2 != 0 and len(arr[i:j]) > 1:
                        sum_arr += sum(arr[i:j + 1])
        return sum_arr