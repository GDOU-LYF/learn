n=int(input())
mapl=[list(map(int,input().split())) for _ in range(n)]
def dfs(row,n,s,mapl):
  global count
  if row==n:
    if s==2:
      dfs(0,n,3,mapl)
    if s==3:
      count+=1
    return
  for i in range(n):
    if mapl[row][i]!=1:
      continue
    if check(row,i,s,mapl):
      mapl[row][i]=s#s=2 白皇后 3 黑皇后
      dfs(row+1,n,s,mapl)
      mapl[row][i]=1

def check(row,col,s,mapl):
  n=len(mapl)
  for i in range(n):
    if mapl[i][col]==s:
      return False
  for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
    if mapl[i][j]==s:
      return False
  for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
    if mapl[i][j]==s:
      return False
  return True
count=0
dfs(0,n,2,mapl)
print(count)