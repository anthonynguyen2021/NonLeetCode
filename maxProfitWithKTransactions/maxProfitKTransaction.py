# Idea of solution: We solve this by DP. The idea is the build a 2D array and build the solution one by one where the rows represent the number of transactions from
# 0, .... , k; and the columns represents day {0, 1, .... , i-1} transactions. At index (i, j), we have either buildDP[i][j] = buildDP[i][j-1] which means that we don't use the
# prices[j] stock or buildDP[i][j] = prices[j] + max_{0 <= k < j}(-prices[k] + buildDP[i-1][k]) - this means that we have chosen prices[j] as (buy or sell) - assume with no
# loss in generality it's a sell. Suppose l = argmax_{0 <= k < j}(-prices[k] + buildDP[i-1][k]). Then we bought prices[l] as one of our transactions and buildDP[i-1][l] have our
# other transactions. The question that prices[l] might not be in our transactions might arise, then buildDP[i-1][l] will have prices[l] to cancel out with -prices[l].

# Why it works: We argue by induction. Assume we fixed i in {0, 1, ..., k}. Assume the results holds for j >= 0. When j = 0,  DP[i][0] = 0. When j = 1, we have 
# DP[i][1] = max(DP[i][0] (equals 0), prices[1] - prices[0]). Note that if we buy at prices[0] and sell at prices[1] and lose profit, the DP[i][1] = 0. We can see that this holds
# by double induction. First, when we induct for i >= 0 and second, when j >= 0. First, set i = 1, and argue by induction. 

# Time = O(kn) | Space = O(kn) where k and n are # of transactions and n = length of prices, respectively.
def maxProfitWithKTransactions(prices, k):
	if not len(prices):
		return 0
    	buildDP = [[0 for _ in prices] for i in range(k+1)]
	for row in range(1, k+1):
		maxSeen = float('-inf')
		for col in range(1, len(prices)):
			maxSeen = max(maxSeen, -prices[col-1] + buildDP[row-1][col-1])
			buildDP[row][col] = max(buildDP[row][col-1], prices[col] + maxSeen)
	return buildDP[-1][-1]
