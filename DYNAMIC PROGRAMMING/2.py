#write  program to find the 5th term in fibonacci series
#dynamic approach
def feb(n): #5
    dp[0]*(n+1) #0 1 1 2 3 5
    dp[0]=0
    dp[1]=1
    for p in range(2, n+1):#(2,6)-->2,3,4,5
        dp[p]=dp[p-1]+dp[p-2] #dp[5]=dp[4]+dp[3] = 3+2=5
    return dp[n]
print(feb(7))