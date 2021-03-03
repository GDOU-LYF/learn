def p(k):
    list1=list()
    for i in range(2,k):
        if k%i==0:
            list1.append(i)
            list1+=list(map(int,p(k//i).split('*')))
            break
    if len(list1)==0:
        list1.append(k)
    
    return '*'.join(str(i) for i in list1)

a,b=map(int,input().split())
for x in range(a,b+1):
    print('{}={}'.format(x,p(x)))