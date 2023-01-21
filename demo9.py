#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
#
class Solution:
    def minMoney(self , arr: List[int], aim: int) -> int:
        nums=arr
        target=aim
        dp = [1000] * (target + 1)
        dp[0] = 0
        # dp[1]=0
        for i in nums:
            for j in range(i, target + 1):
                if (j - i) % i == 0 or dp[j - i] < 1000:
                    dp[j] = min(dp[j - i] + 1, dp[j])
                else:
                    pass
                    # dp[j]=-1
        ff = dp[target]
        if ff == 1000:
            return -1
        elif ff == 0:
            return 0
        else:
            return dp[target]
