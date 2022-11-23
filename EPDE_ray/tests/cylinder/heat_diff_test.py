#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:52:06 2021

@author: maslyaev
"""

import numpy as np
import epde.interface.interface as epde_alg
import pandas as pd

from epde.interface.equation_translator import Coeff_less_equation
from epde.interface.prepared_tokens import Custom_tokens, Cache_stored_tokens
from epde.evaluators import Custom_Evaluator, simple_function_evaluator, inverse_function_evaluator

if __name__ == '__main__':
    t_max = 400
    
    temperature_experimental = pd.read_excel('tests/cylinder/data/Temperature_filtered.xlsx')
    # file = np.loadtxt('/home/maslyaev/epde/EPDE/tests/cylinder/data/Data_32_points_.dat', 
    #                   delimiter=' ', usecols=range(33))
    
    temp_np = temperature_experimental.to_numpy()
    x = np.linspace(1., 10., 5)
    t = temp_np[:t_max, 0]
    grids = np.meshgrid(t, x, indexing = 'ij')
    u = temp_np[:t_max, 1::2]