class Solution(object):
    def findRotation(self, mat, target):
     #Loop through 4 possible rotations
        for n in range(4):
            if(mat == target): # Check if the current matrix matches the target matrix
                return True
            else:
                # Rotate the matrix 90 degrees clockwise
                 for i in range(len(mat)):
                    for j in range(i+1):
                        # Swap elements to transpose the matrix
                         mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
                 for row in mat:
                      row.reverse()  # Reverse each row to complete the 90-degree rotation
        return False
