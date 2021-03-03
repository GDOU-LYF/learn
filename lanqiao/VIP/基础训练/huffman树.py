n=int(input())
mapl=list(map(int,input().split()))
sum=0
while len(mapl)!=1:
    mapl.sort()
    count=mapl[0]+mapl[1]
    sum+=count
    del mapl[1]
    del mapl[0]
    mapl.append(count)
    # print(mapl)
print(sum)
