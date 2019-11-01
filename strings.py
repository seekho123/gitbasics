# Input series of comma-separated strings
s = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l = s.split(', ')
l_rev = list (l)
l_rev.reverse()
l.extend(l_rev)
print (l)