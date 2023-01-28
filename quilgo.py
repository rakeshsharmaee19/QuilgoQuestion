#Python program that finds the longest common substring between two strings
def longestCommanSubString(x,y,m,n):
    longestComman = [[0 for k in range(n+1)] for l in range(m+1)]
    result =0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                longestComman[i][j]==0
            elif x[i-1] == y[j-1]:
                longestComman[i][j] = longestComman[i-1][j-1]+1
                result = max(result, longestComman[i][j])
            else:
                longestComman[i][j] = 0
    return result
            
x = input('enter the first string : ')
y = input('enter the second string : ')
m = len(x)
n = len(y)
print('Length of longest comman substring is ',longestCommanSubString(x,y,m,n))
