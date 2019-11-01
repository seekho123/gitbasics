def convert_object_to_list(obj):
    # your code here
    ll=[]
    
    for k,v in obj.items():
        l = []
        
        l.append(k)
        l.append(v)
        
        ll.append(l)
    
    return ll

inp = {'name': 'Holly', 'age': 35, 'role': 'producer'}
output = convert_object_to_list(inp)
print (output)