def transponeeriK(matrix):
  n = len(matrix[0])
  for i in range(0, n-1):
    for j in range(0, n-1-i):
      matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
  return matrix