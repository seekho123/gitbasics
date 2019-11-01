nums = input('''Please enter a series of numbers separated by commas. \n Hit enter when you are done. ''')
l1=[]
l2=[]
for i,e in enumerate(nums.split(',')):
    if i%2==0:
        l1.append(int(e))
    else:
        l2.append(int(e))
i1 = iter(l1)
i2 = iter(l2)
IC = zip(i1,i2)
res = list(IC)
print (res)