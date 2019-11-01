def modulo(op1,op2):
    '''
    is a number or return None
    flag if op2 is negative
    op2 cannot be 0
    if op1 == 0 return 0
    '''
    
    
    #s1 = str (op1)
    #s2 = str (op2)
    
    #if s1.isdigit() == False or s2.isdigit == False:
     #   return None
    if type (op1) == NoneType:
        return None
    if type (op2) == None:
        return None
    if op2 == 0:
        return None
    

    val =  op1 - ((op1 // op2) * op2)


    
    return val

print(modulo (None,6))