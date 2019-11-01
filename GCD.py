number1 = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))


# Remember to print out the results from lowest to highest
if number1 >0 and number2>0:
    divisor = 1
    GCD =1
    while (divisor <= number1 and divisor<=number2):
        if (number1%divisor == 0) and (number2%divisor == 0):
            GCD = divisor
        divisor += 1
    print (GCD)
else:
    pass



