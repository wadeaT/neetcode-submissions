class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal =[]

        for i in range(numRows):
            current_row = []
            for j in range(0,i+1):
                if i == 0 or j == 0 or j == i:
                    current_row.append(1)
                else:
                    current_row.append(pascal[i-1][j-1]+pascal[i-1][j])
            pascal.append(current_row)
        return pascal