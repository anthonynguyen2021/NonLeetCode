

def longestCommonSubsequence(str1, str2):
	'''
	Time: O(mn * min(m, n)) where m = len(str1), n = len(str2)
	Space: O(mn * min(m, n))

	Explanation brute force DP:

	The idea is if two strings have the same ending character, the problem is reduced to 
	solving the subproblem with the last character of each string removed and append it later.
	Otherwise, we solve the problem dynamically on strings str1[0:len(str1)-1] and str2 or 
	str1 and str2[0:len(str2)-1] as the longest subsequence's last character maybe at the 
	end of str1 or str2. In this case, we take the largest subsequence from the solution of 
	a) str1[0:len(str1)-1] and str2 or b) str1 and str2[0:len(str2)-1]
	'''
	longestDP = [[[] for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

	for i in range(1, len(str1) + 1):
		for j in range(1, len(str2) + 1):

			if str1[i - 1] == str2[j - 1]:
				longestDP[i][j] = longestDP[i - 1][j - 1] + [str1[i - 1]]
			else:
				longestDP[i][j] = max(longestDP[i - 1][j], longestDP[i][j - 1], key = len)

	return longestDP[-1][-1]
