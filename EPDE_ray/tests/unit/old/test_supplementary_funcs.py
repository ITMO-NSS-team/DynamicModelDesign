#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:36:26 2021

@author: mike_ubuntu
"""

import sys
import getopt

global opt, args
opt, args = getopt.getopt(sys.argv[2:], '', ['path='])

sys.path.append(opt[0][1])

import numpy as np
from epde.src.supplementary import Population_Sort

def test_sort():
    class Dummy_Individ():
        def __init__(self, evaluated : bool):
            self.fitness_calculated = evaluated
            if self.fitness_calculated:
                self.fitness_value = np.random.uniform(low = 0., high = 100.)
                print('evaluated?', self.fitness_calculated, 'value', self.fitness_value)
            else:
                print('evaluated?', self.fitness_calculated, 'no value')
 
    population = []
    size_total = 16; size_evald = 10
    for idx in range(size_total):
        evaluated = True if idx < size_evald else False
        population.append(Dummy_Individ(evaluated))
        
    print([individual.fitness_calculated for individual in population])
    population = Population_Sort(population)
    assert population[0].fitness_calculated
    assert population[0].fitness_value > population[1].fitness_value
    assert not population[-1].fitness_calculated