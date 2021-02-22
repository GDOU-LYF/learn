# litle = ['0', '1']
# for a1 in litle:
#     for a2 in litle:
#         for a3 in litle:
#             for a4 in litle:
#                 for a5 in litle:
#                     print('{}{}{}{}{}'.format(a1,a2,a3,a4,a5))
#

for i in range(32):
    a = '0000' + bin(i)[2:]
    print(a[-5:])
