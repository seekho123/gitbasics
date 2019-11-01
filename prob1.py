

def deMorgans(E, F, S):
    '''
    Return, as a tuple of the form (Law A, Law B), each of the sets
    associated with De Morgan's laws as applied to sets E and F.

    Return "Improper Specification" if three sets are not supplied
    or if the events E and F are not subsets of the sample space S.
    
    Parameters
    ----------
    E : {set} First event space
    F : {set} Second event space
    S : {set} Complete sample space

    Returns
    -------
    tuple({set}, {set}) or {str} 

    Example:
    >>> DeMorgans(set([1,2,3]), set([2,3,4]), set([0,1,2,3,4,5]))
    (set([0, 5]), set([0, 1, 4, 5])
    '''


    if check_specs(E, F, S) == "fail":
        return "Improper Specification"
    else:
        law_a = lawA(E, F, S)
        law_b = lawB(E, F, S)
    return (law_a, law_b)



def check_specs(E, F, S):
    if (type (E) == set and
        E <= S          and
        type(F) == set  and
        F <= S          and
        type (S) == set):
            return ("good")
    else:
        return "fail"
                
        


def lawA(E, F, S):
    return (S - E) & (S - F)
    


def lawB(E, F, S):
    return S - (E & F)

a= deMorgans(set([1,2,3]), set([2,3,4]), set([0,1,2,3,4,5]))
print (a)



