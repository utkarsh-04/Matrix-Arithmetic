import numpy as np
class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        
    
        
    def add(self, other):
        return self.matrix + other.matrix

    def transpose(self):
        return np.transpose(self.matrix)

    def subtract(self, other):
        return self.matrix - other.matrix
        
    def multiply(self, other):
        return np.dot(self.matrix, other.matrix)
        
    def determinant(self):
       return np.linalg.det(self.matrix)
            
    def matrix_power(self, power):
        n = len(self.matrix)
        result = np.identity(n)
        while power > 0:
            if power & 1:
                result = np.dot(result, self.matrix)
            matrix = np.dot(self.matrix, self.matrix)
            power >>= 1
        return result


    def inverse(self):
        I = np.identity(len(self.matrix))
        n = len(self.matrix)
        for i in range(n):
            if self.matrix[i][i] == 0:
                for row in range(i+1, n):
                    if self.matrix[row][i] != 0:
                        for col in range(n):
                            self.matrix[row][col], self.matrix[i][col] = self.matrix[i][col], self.matrix[row][col]
                            I[row][col], I[i][col] = I[i][col], I[row][col]
                        break
            dia = self.matrix[i][i]
            for col in range(n):
                self.matrix[i][col] /= dia
                I[i][col] /= dia
            for j in range(n):
                if i == j:
                    continue
                coff = self.matrix[j][i]
                for col in range(n):
                    self.matrix[j][col] -= self.matrix[i][col] * coff
                    I[j][col] -= I[i][col] * coff
        return I
        



matrix1 = Matrix([[1, 2, 3], [4, 6, 0],[7, -1, -9]])
matrix2 = Matrix([[5, 6,7], [7, 8,0],[1,2,3]])

print(matrix1.add(matrix2))

print(matrix1.subtract(matrix2))

print(matrix1.multiply(matrix2))

print(matrix1.transpose())

print(matrix1.inverse())

print(matrix1.determinant())

print(matrix1.matrix_power(6))

