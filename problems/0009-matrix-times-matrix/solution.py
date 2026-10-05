def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              result = []
              if len(a[0]) == len(b):
                for row in range(len(a)):
                    result_row = []
                    for column in range(len(b[0])):
                        dot = 0
                        for pos in range(len(a[0])):
                            dot += a[row][pos] * b[pos][column]
                        result_row.append(dot)
                    result.append(result_row)
                return result
              else:
                return -1

# torch.matmul(a, b)
# np.matmul(a, b)