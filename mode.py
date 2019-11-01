def d_mode(l):
    data_d = {}
    for i in l:
        if i not in data_d.keys():
            data_d[i] = 1
        else:
            data_d[i] += 1
    
    d = max(list(data_d.values()))
    for i,j in data_d.items():
        if j==d:
            return i

print (d_mode ([2,4,5,5,7,7,8,8,8]))
