def transponeeriK(matrix):
    return [[matrix[len(matrix)-1-j][len(matrix[0])-1-i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    

# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# 
# result = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]
# 
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         result[j][i] = matrix[len(matrix)-1-i][len(matrix[0])-1-j]
# 
# for r in result:
#    print(r)