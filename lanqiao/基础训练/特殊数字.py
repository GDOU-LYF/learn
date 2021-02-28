# print(123//100)
# print(123//10%10)
# print(123%10%10)
for i in range(135,1000):
    a=i//100
    b=i//10%10
    c=i%10%10
    if i==a**3+b**3+c**3:
        print(i)