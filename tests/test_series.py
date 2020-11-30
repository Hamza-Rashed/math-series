from series.series import *

"""
Fibonacci test :
     0 => 0
     1 => 1
     5 => 5
     6 => 8

"""

def test_fibonacci1():
    assert fibonacci(0) == 0

def test_fibonacci2():
    assert fibonacci(1) == 1

def test_fibonacci3():
    assert fibonacci(5) == 5

def test_fibonacci4():
    assert fibonacci(6) == 8
###############################################################

"""
Lucas test :
     0 => 2
     1 => 1
     3 => 4
"""

def test_Lucas1():
    assert lucas(0) == 2

def test_Lucas2():
    assert lucas(1) == 1

def test_Lucas3():
    assert lucas(3) == 4

###############################################################
"""
sum_series test :
     8 => 21
     3,8,14 => 49

"""

def test_sum_series1():
    assert sum_series(8) == 21

def test_sum_series2():
    assert sum_series(3, 8, 14) == 49
