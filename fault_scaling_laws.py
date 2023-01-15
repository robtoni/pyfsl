#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
It get 

"""

import math
import os
import sys


def get_fsl_tables(filename):
    """
    Get all info from the two tables prepared by R. Basili:
        1. FaultScalingLawsToGetMw.txt
        2. FaultScalingLawsToGetSize.txt
    and return two arrays organized in keys and 

    """

    if filename == None:
        sys.exit("Input file name error.")
    

    fsl_dir = os.path.dirname(os.path.realpath(__file__))
    fsl = {}
    with open(os.path.join(fsl_dir, filename), 'r') as f:
        for ic, line in enumerate(f.readlines()):
            tmp = line.strip().split("\t")
            if (ic == 0):
                keys = [tmp[i].replace('"','') for i in range(len(tmp))]
            else:
                items = [tmp[i].replace('"','') for i in range(len(tmp))]
                fsl[str(ic)] = {k: v  for (k, v) in zip(keys, items)}
    
    return fsl


def get_magnitude(lc, fd, ft, tc, size, printing=False):
    """
    Input 
        lc: law code (sting)
        fd: fault dimension (string)  
        ft: fault type (string)  
        tc: tectonic code (integer)
        size: selected size of the fault (length/width/area) (float)

    Output
        mu: magnitude
        sigma: associated error (testing)
    """

    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data')) 
    file_get_mag = os.path.join(data_dir, 'FaultScalingLawsToGetMw.txt')
    fsl = get_fsl_tables(file_get_mag)

    for key in fsl.keys():
        if fsl[key]["LawCode"]==lc and   \
           fsl[key]["FaultDim"]==fd and  \
           fsl[key]["FaultType"]==ft and \
           fsl[key]["TectoCode"]==tc: 
           
            isel = key
    #
    a = float(fsl[isel]["A"])
    b = float(fsl[isel]["B"])
    ase = float(fsl[isel]["Ase"])
    bse = float(fsl[isel]["Bse"])
    rse = float(fsl[isel]["Rse"])
    rsq = float(fsl[isel]["Rsq"])
    n = float(fsl[isel]["N"])
    m_min = float(fsl[isel]["MwMin"])
    m_max = float(fsl[isel]["MwMax"])
    size_min = float(fsl[isel]["SizeMin"])
    size_max = float(fsl[isel]["SizeMax"])

    # correction of size_max when SizeMax=0 (no value)
    if size_max < 0.1:
        size_max = 100000.0

    # check size range values
    if size >= size_max or size <= size_min:
#        sys.exit(("The selected size {:s}={:.2f} is out"
#                  " of range ({:.2f}-{:.2f})").format(fsl[key]["FaultDim"], 
#                                               size, size_min, size_max))
        print(("The selected size {:s}={:.2f} is out"
               " of range ({:.2f}-{:.2f})").format(fsl[key]["FaultDim"], 
                                            size, size_min, size_max))
   
    mu = a + b*math.log10(size)
    sigma = rse
    
    if printing:
        print("Selected scaling law: {0}".format(fsl[isel]["Reference"]))
        print("a = {:f}, b = {:f}".format(a, b))

    return mu#, sigma   


def get_fault_size(lc, fd, ft, tc, m, printing=False):
    """
    Input 
        lc: law code (sting)
        fd: fault dimension (string)  
        ft: fault type (string)  
        tc: tectonic code (integer)
        m: magnitude (float)

    Output
        mu: selected size of the fault (lenght/width/area) (float)
        sigma: associated error (testing)
    
    """
    
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data')) 
    file_get_size = os.path.join(data_dir, 'FaultScalingLawsToGetSize.txt')
    fsl = get_fsl_tables(file_get_size)

    for key in fsl.keys():
        if fsl[key]["LawCode"]==lc and   \
           fsl[key]["FaultDim"]==fd and  \
           fsl[key]["FaultType"]==ft and \
           fsl[key]["TectoCode"]==tc: 
           
            isel = key
    #
    a = float(fsl[isel]["A"])
    b = float(fsl[isel]["B"])
    ase = float(fsl[isel]["Ase"])
    bse = float(fsl[isel]["Bse"])
    rse = float(fsl[isel]["Rse"])
    rsq = float(fsl[isel]["Rsq"])
    n = float(fsl[isel]["N"])
    m_min = float(fsl[isel]["MwMin"])
    m_max = float(fsl[isel]["MwMax"])
    size_min = float(fsl[isel]["SizeMin"])
    size_max = float(fsl[isel]["SizeMax"])

    # correction of m_max when MwMax=0 (no value)
    if m_max < 0.1:
        m_max = 10.0
        
    # check magnitude range values
    if m >= m_max or m <= m_min:
#        sys.exit(("The selected magnitude M={:.2f} is out"
#                  " of range ({:.2f}-{:.2f})").format(m, m_min, m_max))
        print(("The selected magnitude M={:.2f} is out"
               " of range ({:.2f}-{:.2f})").format(m, m_min, m_max))

    mu = math.pow(10, (a + b*m))
    sigma = math.pow(10, rse)
    
    if printing:
        print("Selected scaling law: {0}".format(fsl[isel]["Reference"]))
        print("a = {:f}, b = {:f}".format(a, b))
    
    return mu#, sigma   


    
    

