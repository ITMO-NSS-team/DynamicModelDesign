#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:14:57 2021

@author: mike_ubuntu
"""

from dataclasses import dataclass
import warnings

import ray

from epde.cache.cache import Cache
from epde.cache.cache_actor import Ray_Cache_Actor

@dataclass
class Verbose_Manager:
    plot_DE_solutions : bool
    show_iter_idx : bool
    show_iter_fitness : bool
    show_iter_stats : bool
    show_warnings : bool
    show_moeadd_epochs : bool


@ray.remote
class Verbose_Manager_Actor(object):
    def __init__(self, plot_DE_solutions, show_iter_idx, show_iter_fitness,
                              show_iter_stats, show_warnings, show_moeadd_epochs):
        self.verbose = Verbose_Manager(plot_DE_solutions, show_iter_idx, show_iter_fitness, 
                                       show_iter_stats, show_warnings, show_moeadd_epochs)
    
    def get(self):
        return self.verbose


def init_verbose(plot_DE_solutions : bool = False, show_iter_idx : bool = False, 
                 show_iter_fitness : bool = False, show_iter_stats : bool = False, 
                 show_warnings : bool = False, show_moeadd_epochs : bool = False):
    global verbose
    if not show_warnings:
        warnings.filterwarnings("ignore")

    verbose = Verbose_Manager_Actor.remote(plot_DE_solutions, show_iter_idx, show_iter_fitness,
                                               show_iter_stats, show_warnings, show_moeadd_epochs)
    # verbose = ray.get(verbose_rem) _rem
    # else:
    #     verbose = Verbose_Manager(plot_DE_solutions, show_iter_idx, show_iter_fitness,
    #                               show_iter_stats, show_warnings, show_moeadd_epochs)


@ray.remote
class Global_States(object):
    def __init__(self, parallelize : bool = True, time_axis : int = 0):
        self.set_state(parallelize, time_axis)
        
    def set_state(self, parallelize : bool, time_axis : int):
        self._parallelize = parallelize
        self._time_axis = time_axis
        
    def parallelize(self):
        return self._parallelize
    
    def time_axis(self):
        return self._time_axis


def init_globals(parallelize : bool = True, time_axis : int = 0, set_grids : bool = False):
    global tensor_cache, grid_cache, states
    states = Global_States.remote(parallelize, time_axis)
    # print(type(states_rm))
    # states = ray.get(states_rm)
    
    tensor_cache = Cache()
    if set_grids:
        grid_cache = Cache()
    else:
        grid_cache = None
    
    if parallelize:
        global tensor_cache_actor, grid_cache_actor
        tensor_cache_actor = Ray_Cache_Actor.remote(tensor_cache)
        # tensor_cache_actor = ray.get(tensor_cache_actor_rm)
        if set_grids:
            grid_cache_actor = Ray_Cache_Actor.remote(tensor_cache)
            # grid_cache_actor = ray.get(grid_cache_actor_rm)


def set_time_axis(axis : int):
    global time_axis
    time_axis = axis


def init_eq_search_operator(operator):
    global eq_search_operator
    eq_search_operator = operator


def init_sys_search_operator(operator):
    global sys_search_operator
    sys_search_operator = operator


def delete_cache():
    global tensor_cache, grid_cache
    try:
        del tensor_cache
    except NameError:
        print('Failed to delete tensor cache due to its inexistance')
    try:
        del grid_cache
    except NameError:
        print('Failed to delete grid cache due to its inexistance')