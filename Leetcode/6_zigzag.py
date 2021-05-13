def convert(s: str, numRows: int) -> str:
    slen = len(s)
    up = True
    row = 1
    rows = {}
    answer = ""
    if numRows == 1:
        return s
    else:
        for x in range(slen):
            if x == 0:
                rows[row] = s[x]
            elif up:
                row += 1
                if row in rows:
                    rows[row] += s[x]
                else:
                    rows[row] = s[x]
                if row == numRows:
                    up = False
            else:
                row -= 1
                if row in rows:
                    rows[row] += s[x]
                else:
                    rows[row] = s[x]
                if row == 1:
                    up = True
        for x in range(1, 1 + numRows):
            if x in rows:
                answer += rows[x]
        return answer

print(convert("PAYPALISHIRING", 3))
