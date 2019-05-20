def minDist(word1, word2):
	len1 = len(word1)
	len2 = len(word2)
	dp = [[0 for i in range(len1+1)] for j in range(len2+1)]
	print(dp)    # 构造dp矩阵 

	i = 0 
	for item in dp:
		item[0] = i
		i += 1
	i = 0
	for i in range(len1+1):
		dp[0][i] = i
		i += 1

	for i in range(1, len1+1):

		for j in range(1, len2+1):
			if word1[i-1] == word2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				insert = 1 + dp[i][j-1]
				delete = 1 + dp[i-1][j]
				replace = dp[i-1][j-1] + 1
				dp[i][j] = min(insert, delete, replace)
	return dp



if __name__ == '__main__':
	word1 = 'much'
	word2 = 'more'
	dp = minDist(word1, word2)
	for i in dp:
		print(i)
