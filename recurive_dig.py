def rec_dig_sum(n):
    '''
    Returns the recursive digit sum of an integer.

    Parameter
    ---------
    n: int

    Returns
    -------
    rec_dig_sum: int
       the recursive digit sum of the input n
    '''
    n_digits = [int(d) for d in str(n)]
    
    if len(n_digits) == 1:
    	return n
    
    
    d_sum = 0
    
    for i in n_digits:
      d_sum += i
      
    ds = rec_dig_sum (d_sum)
    
    return ds
      
    
    


def distr_of_rec_digit_sums(low=0, high=1500):
    '''
    Returns a dictionary representing the counts
    of recursive digit sums within a given range.

    Parameters
    ----------
    low: int
        a positive integer representing the lowest
        value in the range of integers for which finding
        the recursive digit sum
    high: int
        a positive integer greater than low, the inclusive
        upper bound for which finding the recursive digit sum

    Returns
    -------
    dict_of_rec_dig_sums: {int:int}
        returns a dictionary where the keys are the recursive
        digit sums and the values are the counts of those digit sums
        occurring
    '''
    
    dic = dict()
    
    for i in range(low, high+1):
      d_sum = rec_dig_sum(i)
      print (d_sum)
      if d_sum not in dic.keys():
        dic[d_sum]= 1
      else:
        dic[d_sum] +=1
        
    return dic


d=distr_of_rec_digit_sums(9,11)
print (d)


