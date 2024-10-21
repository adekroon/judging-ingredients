# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:42:37 2024

@author: Akari Surface
"""

def test_check_flour_quantity():
    assert check_flour_quantity(500) == 'correct flour quantity'
    assert check_flour_quantity(' ') == 'String input not accepted'
    
def test_check_flour_type():
    assert check_flour_type('white flour')=="this flour type shouldn't be used. you should use all-purpose flour, bread flour, whole wheat flour, or white whole wheat flour"
  
def test_check_water_quantity():
    assert check_water_quantity(400)=='too much water. you should use 300ml of water'

def test_check_milk_quantity():
    assert check_milk_quantity(100)=="don't need milk"

def test_check_salt_quantity():
    assert check_salt_quantity(1)=='too little salt. you should use 2 tsp of salt'
 
def test_check_yeast_quantity():
    assert check_yeast_quantity(6)=='too little yeast. you should use 7g of yeast'

def test_check_oil_quantity():
    assert check_oil_quantity(4)=='too much oil. you should use 3 tbs of oil'

def test_check_oil_type():
    assert check_oil_type('vegetable oil')== "this oil type shouldn't be used. you should use olive oil or coconut oil"

def test_check_egg_quantity():
    assert check_egg_quantity(1)=="don't need eggs"




def check_flour_quantity(num):
    """
    Parameters
    ----------
    num : numeric (in grams)
    
    Returns
    -------
    str : decision/judgement if flour quantity is sufficient to make bread 

    """
    if isinstance(num, str):
        return "String input not accepted"
    
    if num == 500:
        return 'correct flour quantity'
    elif num > 500:
        return 'too much flour. you should use 500g of flour'
    else:
        return 'too little flour. you should use 500g of flour'
   

def check_flour_type(flour_type):
    """
    Parameters
    ----------
    flour_type : string (in quotation marks)

    Returns
    -------
    str : decision/judgement if flour type can be used to make bread

    """
    correct_flourlist = ['All-purpose flour', ' all purpose flour', 'All purpose flour', 'all-purpose flour','all purpose flour', "bread flour", ' bread flour', ' whole wheat flour',"whole wheat flour","white whole wheat flour"]
    if flour_type in correct_flourlist:
        return 'correct flour type'
    else: 
        return "this flour type shouldn't be used. you should use all-purpose flour, bread flour, whole wheat flour, or white whole wheat flour"
    
def check_water_quantity(num):
    """
    Parameters
    ----------
    num : numeric (in ml)

    Returns
    -------
    str : decision/judgement if water quantity is sufficient to make bread

    """
    if num == 300:
        return 'correct water quantity'
    elif num > 300: 
        return 'too much water. you should use 300ml of water'
    else: 
        return 'too little water. you should use 300ml of water'
    

def check_milk_quantity(num):
    """
    Parameters
    ----------
    num : numeric (in ml)

    Returns
    -------
    str : decision/judgement if milk quantity is sufficient to make bread

    """
    if num == 0:
        return 'correct milk quantity'
    else: 
        return "don't need milk"


def check_salt_quantity(num):
    """
    Parameters
    ----------
    num : numeric (in teaspoons)

    Returns
    -------
    str : decision/judgement if salt quantity is sufficient to make bread

    """
    if num == 2:
        return 'correct salt quantity'
    elif num > 2:
        return 'too much salt. you should use 2 tsp of salt'
    else: 
        return 'too little salt. you should use 2 tsp of salt'
    


def check_yeast_quantity(num):
    """
    Parameters
    ----------
    num : numeric (in grams)

    Returns
    -------
    str : decision/judgement if yeast quantity is sufficient to make bread
    
    """
    if num == 7:
        return 'correct yeast quantity'
    elif num > 7:
        return 'too much yeast. you should use 7g of yeast'
    else: 
        return 'too little yeast. you should use 7g of yeast'


    
def check_oil_quantity(num):
    """
    Parameters
    ----------
    num : numeric (in tablespoons)

    Returns
    -------
    str : decision/judgement if oil quantity is sufficient to make bread

    """
    if num == 3:
        return 'correct oil quantity'
    elif num > 3:
        return 'too much oil. you should use 3 tbs of oil'
    else:
        return 'too little oil. you should use 3 tbs of oil'
    

    
def check_oil_type(oil_type):
    """
    Parameters
    ----------
    oil_type : string (in quotation marks)

    Returns
    -------
    str : decision/judgement if oil type can be used to make bread

    """
    correct_oillist = ['olive oil', 'Olive oil', 'coconut oil', 'Coconut oil']
    if oil_type in correct_oillist:
        return 'correct oil type'
    else: 
        return "this oil type shouldn't be used. you should use olive oil or coconut oil"
    


def check_egg_quantity(num):
    """
    Parameters
    ----------
    num : numeric integer

    Returns
    -------
    str : decision/judgement if egg quantity can be used to make bread

    """
    if num == 0:
        return 'correct egg quantity'
    else:
        return "don't need eggs"
    
