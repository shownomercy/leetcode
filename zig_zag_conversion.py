class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s

        current_col = 0
        current_row = -1
        going_down = True
        index = 0
        result_list = []
        for c in s:
            if (going_down):
                current_row += 1
            else:
                current_row -= 1
                current_col += 1
            if (current_row == numRows - 1):
                going_down = False
            elif (current_row == 0):
                going_down = True

            result_list.append((index, current_row, current_col))
            index += 1

        sorted_result = sorted(
            result_list, key=lambda element: (element[1], element[2]))

        out_put = ''
        for t in sorted_result:
            out_put += s[t[0]]
        return out_put


s = Solution()
s.convert("PAYPALISHIRING", 4)
