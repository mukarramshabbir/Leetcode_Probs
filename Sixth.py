def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or len(s)<=numRows:
        return s

    # Create empty strings for each row
    rows = [''] * numRows

    # Variables for tracking the current row and direction
    current_row = 0
    direction = 1  # 1 for moving down, -1 for moving up

    # Traverse the string and append characters to the appropriate row
    for char in s:
        rows[current_row] += char
        current_row += direction

        # Change direction when reaching the top or bottom row
        if current_row == 0 or current_row == numRows - 1:
            direction *= -1

    # Concatenate all rows to form the final zigzag pattern
    return ''.join(rows)
            
if __name__=="__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    result = convert(s, numRows)
    print(result) 