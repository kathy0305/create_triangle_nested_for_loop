
def triple_nest(size=5):
    box=""
    for i in range(1,size+1):                   #big loop will start line (1-6)
        line=""
        for j in range (size-1):        #small loop to  add '.' reverse count
            line=line +'.'
        for m in range (i):             #small loop to add the string value of i
            line=line+str(i)
        line=line+"\n"                  #go back to big loop and add line break
        box=box+line
    return box
