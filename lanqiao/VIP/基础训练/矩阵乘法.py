n,m=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(n)]
#阶乘 
def MatrixMultiply(a,n,m,array=None):
    if array is None:
        array=a
    array_return=[[0]*n for _ in range(n)]
    if m==1:
        return a
    elif m==0:#0阶矩阵==单位矩阵
        #令对角线=1
        for i in range(n):
            array_return[i][i]=1
        return array_return
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    array_return[i][j]+=a[i][k]*array[k][j]
        return MatrixMultiply(array_return,n,m-1,array)                    

array=MatrixMultiply(array,n,m)
for row in array:
    for col in row:
        print(col,end=' ')
    print()