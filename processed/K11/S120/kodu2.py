#
#  A B C   I F C
#  D E F   H E B
#  G H I   G D A
#

def transponeeriK(matrix):
    output_matrix = []
    for col in range(len(matrix[0])-1, -1, -1):
        changed_row = []
        for row in range(len(matrix)-1, -1, -1):
            changed_row.append(matrix[row][col])
        output_matrix.append(changed_row)

    return output_matrix