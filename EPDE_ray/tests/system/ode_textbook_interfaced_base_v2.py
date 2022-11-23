#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:51:34 2021

@author: mike_ubuntu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:45:14 2021

@author: mike_ubuntu
"""
import epde.interface.interface as epde_alg
from epde.interface.prepared_tokens import Trigonometric_tokens

#_v2 - epi data, load from txt, visualization of data


import numpy as np
import pandas as pd

def loadDataArray(path, key, len):
    #Extracting an array from a database stored in a txt-file

    df = pd.read_csv(path, delimiter='\t')
    arr = list(df[key])[:len]
    return arr

def calcTotalRegCases(list1):
    #Summing up daily or weekly confirmed cases
    list2 = []
    list2.append(list1[0])
    sum = list1[0]
    for i in range(1, len(list1)):
        sum += list1[i]
        list2.append(sum)

    return list2


import matplotlib.pyplot as plt

if __name__ == '__main__':

    path = 'Test_data/spb.combined.weekly.txt'
    u_raw = loadDataArray(path, key = "CONFIRMED", len = 23)  # loading data with the solution of ODE

    N = len(u_raw)
    print(N)

    u = [np.array(calcTotalRegCases(u_raw))] #Preparing cumulative incidence and fitting the input to the .fit function format

    t = np.linspace(0, 4*np.pi, N) # setting time axis, corresonding to the solution of ODE

    # plt.plot(t, u[0])
    # plt.show()
    
    # Trying to create population for mulit-objective optimization with only 
    # derivatives as allowed tokens. Spoiler: only one equation structure will be 
    # discovered, thus MOO algorithm will not be launched.
    
    epde_search_obj = epde_alg.epde_search()

    trig_tokens = Trigonometric_tokens(freq = (0.95, 1.05))

    epde_search_obj.fit(data = u, equation_factors_max_number = 1, coordinate_tensors = [t,],
                         additional_tokens = [], equation_terms_max_number = 3, max_deriv_order=2, field_smooth = False)

    epde_search_obj.equation_search_results(only_print = True, level_num = 1) # showing the Pareto-optimal set of discovered equations