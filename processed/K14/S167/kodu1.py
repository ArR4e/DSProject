jar = [1, [-2], 3]
#jar = [1, [-2, 6, [-3]], 3]


def rek_abs(jar):
    t = []
    for i in range(0, len(jar)):
        d = jar[i]
        if isinstance(d, list) == False:
            t.append(abs(d))
        if isinstance(d, list) == True:
            t.append(rek_abs(d))
    return t
print(rek_abs(jar))


# t = []
# for i in range(0, len(jar)):
#     d = jar[i]
#     if isinstance(d, list) == False:
#         t.append(abs(d))
#     if isinstance(d, list) == True:
#         t1 = []
#         for i in range(0, len(d)):
#             d = d[i]
#             if isinstance(d, list) == False:
#                 t1.append(abs(d))
#         t.append(t1)



# t = []
# for i in jar: 
#     if isinstance(i, list) == False:
#         t.append(abs(i))
#     if isinstance(i, list) == True:
#         t1 = []
#         for i1 in i:
#             if isinstance(i1, list) == False:
#                 t1.append(abs(i1))
#             if isinstance(i1, list) == True:
#                 t2 = []
#                 for i2 in i1:
#                     if isinstance(i2, list) == False:
#                         t2.append(abs(i2))
#         t1.append(t2)
#         t.append(t1)
# print(t)