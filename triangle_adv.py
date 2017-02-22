def advanced_nested_triangle(start=1, last=5, char='*'):
    box=""
    for i in range(start, last+1):
        line=""
        for j in range(i):
            line = ( char * (j+1))
            line= line +"\n"
        box =box+line
    return box
    
