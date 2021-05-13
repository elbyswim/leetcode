def timeConversion(s):
    #
    # Write your code here.
    #
    return str(int(s[0:2]) % 12 + 12 if s[8:10] == 'PM' else 0) + s[2:8]

print(timeConversion('12:00:00AM'))
print(timeConversion('07:05:45PM'))

