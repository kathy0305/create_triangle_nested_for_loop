def inverted_triangle():
    row =5
    char ='*'
    box=""
    j=1
    for i in range  (row):
        line=""
        for j in range (row-i):
            line = line + char
        line = line +"\n"               # line break out j loop
        box= box +line
    return box
