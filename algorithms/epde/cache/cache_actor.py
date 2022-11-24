#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:17:59 2021

@author: maslyaev
"""

import ray

@ray.remote
class Ray_Cache_Actor(object):
    def __init__(self, cache):
        self.cache = cache

    def call_cache_method(self, method, *args, **kwargs):
        '''
        Parameters:
            method : str,
            Name of the called cache method;
        '''
        return getattr(self.cache, method)(*args, **kwargs)

        