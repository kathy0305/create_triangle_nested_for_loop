def triangle():
    row=5
    char='*'
    box=""
    j=1
    for i in range (row+1):
        line=""
        for j in range(i):
            line=(char*(j+1))
            line=line +"\n"         ## the line break in the first loop
        box=box+line
    return box
  
