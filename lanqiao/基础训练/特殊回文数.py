n=int(input())
for i in range(10000,1000000):
    strl=str(i)
    if strl==strl[::-1]:
        sum=0
        for i2 in strl:
            sum+=int(i2)
        if sum==n:
            print(i)