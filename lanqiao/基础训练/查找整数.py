n=int(input())
list1=list(map(int,input().split()))
a=int(input())
flag=-1
for i in range(len(list1)):
    if a==list1[i]:
        flag=i+1
        break
print(flag)