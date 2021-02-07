class Solution:
    def countLargestGroup(self, n: int) -> int:
        ans = dict()
        answer = 0
        for i in range(1, n +1):
            ans.setdefault((sum(map(int,str(i)))),[]).append(i)
        z = max(map(len, ans.values()))
        for i in ans.keys():
            if z == len(ans[i]):
                answer += 1
        return answer