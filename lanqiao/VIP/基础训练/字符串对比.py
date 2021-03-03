str1=input()
str2=input()
if len(str1)!=len(str2):
    print(1)
elif str1==str2:
    print(2)
elif str1.upper()==str2.upper():
    print(3)
else:
    print(4)