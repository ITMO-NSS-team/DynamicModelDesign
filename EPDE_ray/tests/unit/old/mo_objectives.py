#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:07:01 2021

@author: mike_ubuntu
"""

import sys
import getopt

global opt, args
opt, args = getopt.getopt(sys.argv[2:], '', ['path='])

sys.path.append(opt[0][1])


import numpy as np
from collections import OrderedDict


import epde.src.globals as global_var
from epde.src.token_family import Token_family, Evaluator
from epde.src.factor import Factor
from epde.src.cache.cache import upload_grids, upload_simple_tokens
from epde.src.supplementary import Define_Derivatives

def test_quality():
    pass