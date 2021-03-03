n=int(input())
N=[1]
for i in range(n):
    print(' '.join(str(x) for x in N))
    N.append(0) #在后边加0
    N=[N[k]+N[k-1] for k in range(len(N))]
