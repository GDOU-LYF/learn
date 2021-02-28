#chr(int) ord(str)
n,m=map(int,input().split())
str1=[]
for i in range(m):
    str1.append(chr(ord('A')+i))
for j in range(len(str1)):
    print(str1[j],end='')
print()
for k in range(1,n):
    str1.insert(0,chr(ord('A')+k))#插入
    str1.pop()#弹出
    for p in range(len(str1)):
        print(str1[p],end='')
    print()


# a=ord('A') --70 point
# for i in range(n):
#     first=a+i
#     for k in range(i):
#         print(chr(first-k),end='')
#     for j in range(m-i):
#         print(chr(a+j),end='')
#     print()