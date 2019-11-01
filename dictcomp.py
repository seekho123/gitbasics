nums = input('''Please enter a series of numbers separated by '-'. \n Hit enter when you are done. ''')
l = list( nums.split(' -'))
li=[]
for i in l:
    li.append(int(i))
d = {e: e*e for e in li }