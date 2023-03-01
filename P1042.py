# P1042 [NOIP2003 普及组] 乒乓球

inputs = list()
end=False

while not(end):
    a=input()
    if a:
        for aa in a[:]:
            if aa=='W' or aa=='L':
                inputs.append(aa)
            elif aa=='E':
                end=True
                break
    else:
        end=True
        break

def p(n:int)->None:
    #output=False
    w=l=0
    for i in inputs:
        if i=='W':
            w+=1
        elif i=='L':
            l+=1
        
        if abs(w-l)>=2 and max(w,l)>=n:
            print("{0}:{1}".format(w,l))
            output=True
            w=l=0
        
    #if w!=0 or l!=0 or not(output):
    #    print("{0}:{1}".format(w,l))
    print("{0}:{1}".format(w,l))

p(11)
print()
p(21)
