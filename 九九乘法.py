
##for i in range(1,10):
##    for j in range(1,10):
##        print( i ,'*', j ,'=' ,i*j)

def p(rows):
    for i in range(rows):
        print(''*(rows-i)+'*'*(i+1))
    for j in range(rows-1.0,-1):
        print(''*(rows-j)+'*'*(j))
        

