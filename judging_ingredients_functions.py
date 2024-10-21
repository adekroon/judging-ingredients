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
        return 'correct flour quantity'
    elif num > 500:
        return 'too much flour. you should use 500g of flour'
    else:
        return 'too little flour. you should use 500g of flour'


def test_check_flour_quantity():
    assert check_flour_quantity(500) == 'correct flour quantity'
    assert check_flour_quantity(' ') == 'too little flour. you should use 500g of flour'
test_check_flour_quantity()     

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
    
    
def test_check_flour_type():
    assert check_flour_type('white flour')=="this flour type shouldn't be used"
test_check_flour_type()  

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
    
def test_check_water_quantity():
    assert check_water_quantity(400)=='too much water. you should use 300ml of water'
test_check_water_quantity()

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

def test_check_milk_quantity():
    assert check_milk_quantity(100)=="don't need milk"
test_check_milk_quantity()

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
    
def test_check_salt_quantity():
    assert check_salt_quantity(1)=='too little salt. you should use 2 tsp of salt'
test_check_salt_quantity()

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

def test_check_yeast_quantity():
    assert check_yeast_quantity(6)=='too little yeast. you should use 7g of yeast'
test_check_yeast_quantity()
    
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
    
def test_check_oil_quantity():
    assert check_oil_quantity(4)=='too much oil. you should use 3 tbs of oil'
test_check_oil_quantity()
    
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
    
def test_check_oil_type():
    assert check_oil_type('vegetable oil')== "this oil type shouldn't be used. you should use olive oil or coconut oil"
test_check_oil_type()

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
    
def test_check_egg_quantity():
    assert check_egg_quantity(1)=="don't need eggs"
test_check_egg_quantity()



def main():
    """
    user interface
    uses defined functions to judge whether quantity and/or type of ingredients are suitable to make bread
    several inputs will run, whose user input is stores as a variable that will run through functions which determine whether quantity/type is suitable to make bread
    
    """
    flourqn = input("Enter quantity of flour you want to use (in grams):")
    print(check_flour_quantity(int(flourqn)), '\n')
    
    flourtype = input("Enter type of flour you want to use:")
    print(check_flour_type(flourtype), '\n')
    
    waterqn = input("Enter quantity of water you want to use (in ml):")
    print(check_water_quantity(int(waterqn)), '\n')
    
    milkqn = input("Enter quantity of milk you want to use (in ml):")
    print(check_milk_quantity(int(milkqn)), '\n')

    saltqn = input("Enter quantity of salt you want to use (in teaspoons):") 
    print(check_salt_quantity(int(saltqn)), '\n')
    
    yeastqn = input("Enter quantity of yeast you want to use (in grams):")
    print(check_yeast_quantity(int(yeastqn)), '\n')
    
    oilqn = input("Enter quantity of oil you want to use (in tablespoons):")
    print(check_oil_quantity(int(oilqn)), '\n')
    
    oiltype = input("Enter type of oil you want to use:")
    print(check_oil_type(oiltype), '\n')
    
    eggqn = input("Enter quantity of eggs you want to use (whole numbers):")
    print(check_egg_quantity(int(eggqn)), '\n')
    
main()