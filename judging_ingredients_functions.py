# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:29:13 2024

@author: Akari de Kroon 
"""

def check_flour_quantity(num):
    """
    Parameters
    ----------
    num : numeric (in grams)
    
    Returns
    -------
    str : decision/judgement if flour quantity is sufficient to make bread 

    """
    if num == 500:
        return 'right flour quantity'
    elif num > 500:
        return 'too much flour'
    else:
        return 'too little flour'


def test_check_flour_quantity():
    assert check_flour_quantity(500)=='right flour quantity'
    

def check_flour_type(flour_type):
    """
    Parameters
    ----------
    flour_type : string 

    Returns
    -------
    str : decision/judgement if flour type can be used to make bread

    """
    correct_flourlist = ['all-purpose flour',"bread flour","whole wheat flour","white whole wheat flour"]
    if type in correct_flourlist:
        return 'correct flour type'
    else: 
        return "this flour type shouldn't be used"
    
    
def test_check_flour_type():
    assert check_flour_type('white flour')=="this flour type shouldn't be used"
    