def edit_distance(s1: str, s2: str) -> int:
    """ Returns the minimum number of edits between the strings. """
    m = len(s1)
    n = len(s2)
    
    # 1. Properly initialize the 2D grid with unique rows
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            # 2. Correctly handle the base cases (empty string comparisons)
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            # 3. Use 1-based indexing for dp and 0-based indexing for strings
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                
    # 4. Return the correct bounds using the 'dp' variable name
    return dp[m][n]
