def greet_customer(firstName, customerData):
    # your code here
    
    if firstName is None:
        return
    if customerData is None:
        return
    
    for k,v in customerData.items():
        if k == firstName:
            if v['visits'] == 1:
                print(f'''Welcome back, {firstName}! We're glad you liked us the first time!''')
                break
            if v['visits'] >1:
                print(f'''Welcome back, {firstName}! So glad to see you again!''')
                break
    else:
        print('Welcome! Is this your first time?')

customerData = {'Joe': {'visits': 1},
  'Carol': {'visits': 2},
  'Howard': {'visits': 3},
  'Carrie': {'visits': 4}}
greet_customer ('Carol',customerData)