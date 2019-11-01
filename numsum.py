# your code here
def sum_digits(n):
    nn =n
    if n<0:
        neg = True
        nn = -nn
    
    nl = [int(d) for d in str(nn)]
    ss = sum(nl)
    print (ss)
    
    if neg:
        first_d = nl.pop(0)
        print(first_d)
        ss -= 2*first_d



    
    return ss

print(sum_digits(-1091))
