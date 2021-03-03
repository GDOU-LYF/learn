s=int(input())
h=s//60//60
m=(s-h*60*60)//60
s-=h*60*60+m*60
print('{}:{}:{}'.format(h,m,s))