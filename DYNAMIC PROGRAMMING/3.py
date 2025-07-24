def css(s1,s2): #abcdaf, gbcdf
    m=len(s1)#rows
    n=len(s2)#col
    dp=[[0]*(n+1) for p in range(m+1)]
    max_index=0
    for i in range(m): #0,1,2,3,45-->d
        for j in range(n):#gbcdf
            if s1[i]==s2[j]: #f ,i=5,j=4
                dp[i+1][j+1]=dp[i][j]+1 #dp[6][5]=dp[5][4]+1=1
                max_index=max(max_index,dp[i+1][j+1])
    return max_index

s1 = input()  # abcdaf
s2 = input()  # gbcdf
m=css(s1, s2)
print(m)  # Output: 2 (common subsequence "bd")



#use print(dp) after 2nd for loop to see the dp table