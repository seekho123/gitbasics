number = int(input('Please enter a value for N: '))

 
result = a_old = 1
count = 1
while count<=number:
    result = (2 * a_old) + 1
    print (count," ", result)
    a_old = result
    count +=1
    
# Use print() to print the result, like this:
print(result)