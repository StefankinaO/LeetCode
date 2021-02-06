class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        bool_ans = False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j] * 2 and i != j:
                   
                    bool_ans = True
        return bool_ans
