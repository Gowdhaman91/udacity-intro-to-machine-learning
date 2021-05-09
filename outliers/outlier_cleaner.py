#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    import numpy as np
    from operator import itemgetter

    preds = np.concatenate(predictions)
    ages_tr = np.concatenate(ages)
    net_worths_tr = np.concatenate(net_worths)
    error = abs(net_worths_tr - preds)
    l = list(zip(ages_tr, net_worths_tr, error))
    cleaned_data = sorted(l, key = itemgetter(2))[0:int(0.9*len(l))]

    return cleaned_data

