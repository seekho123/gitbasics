def positive_test(TP, FP, perc_population):
    '''
    Parameters
    ----------
    TP: {float} true positive
        percentage of tests that were positive
        for the sample of subjects that had the disease
    FP: {float} false positive
        percentage of tests that were positive
        for the control population (disease-free subjects)

    percent_population : {float} percentage of the population that has the 
    disease

    Returns
    -------
    {float} probability of having the disease for a person with a positive 
    test result
    '''
    TP_count = TP/100 * perc_population/100
    FP_count = FP/100 * (1.0 - (perc_population/100))
    disease_prob = TP_count/(TP_count+FP_count)
    #print(TP,TP_count)
    #print(FP,FP_count)
    return round(disease_prob,3)

#dis = positive_test(99.5,10.0,.02)
#print (dis)
    