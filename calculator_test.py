import pytest
from calculator import Calculator

calc = Calculator()

#Add 
def test_add1():
  assert calc.add(7,3) == 10

def test_add2():
  assert calc.add(-5,-3) == -8

def test_add3():
  assert calc.add(3,0) == 3

#Subtract
def test_subtract1():
  assert calc.subtract(10,3) == 7

def test_subtract2():
  assert calc.subtract(-5,-3) == -2

def test_subtract3():
  assert calc.subtract(5,0) == 5

#Multiply
def test_multiply1():
  assert calc.multiply(4,3) == 12

def test_multiply2():
  assert calc.multiply(-3,4) == -12

def test_multiply3():
  assert calc.multiply(5,0) == 0

#Divide

def test_divide1():
  assert calc.divide(10,2) == 5
  
def test_divide2():
  assert calc.divide(-10,2) == -5
  
def test_divide3():
  with pytest.raises(ValueError):
    calc.divide(10,0) 
