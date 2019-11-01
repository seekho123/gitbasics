number1 = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))


# Remember to print out the results from lowest to highest
if number1 >0 and number2>0:
    max=number1*number2
    multiplier = 1
    LCM = max
    if number1<=number2:
        LM = number1
        NUM = number2
    else:
        LM = number2
        NUM = number1
   
    while (LM <= max):
        LM *= multiplier
        if (NUM%LM == 0):
            LCM = LM
            break
        multiplier +=1
    print (LCM)
else:
    pass



