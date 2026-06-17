class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        r,c = numRows, len(s)

        matrix = [["" for _ in range(c)] for _ in range(r)]
        count=0
        row, col=0, 0
        while(count<len(s)):
            while row < r and count < len(s):
                matrix[row][col] = s[count]
                count+=1
                row+=1

            row-=2
            col+=1

            while row>0 and col<c and count<len(s):
                matrix[row][col] = s[count]
                count+=1
                col+=1
                row-=1
        res=[]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] != "":
                    res.append(matrix[i][j])
        return "".join(res)