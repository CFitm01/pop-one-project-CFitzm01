import pytest
import shift_cities
import swap_cities
import compute_total_distance
import copy
#from cities import *


road_map = [("Alabama", "Birmingham", 1.23, -4.55),\
            ("Hawaii", "Honolulu", 21.31, -157.83),\
            ("Arkansas", "Little Rock", 34.74, -69.77)]

#
def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)] 
    distance = compute_total_distance.compute_total_distance(road_map1)
    
    assert distance == pytest.approx(9.386+18.496+10.646, 0.01)
    assert distance > 0
#
#    '''add your further tests'''
#
def test_swap_cities():
    #We want to ensure that the cities have indeed swapped
    #Further we want to ensure that the length is not changed,
    #nothing added or lost.
    road_map1 = copy.deepcopy(road_map)
    swap_cities.swap_cities(road_map1, 0, 2)
    assert len(road_map1) == len(road_map)
    assert road_map1[0] != road_map[0]
    assert road_map1[1] == road_map[1]
    '''add your tests'''
#
def test_shift_cities():
    road_map1 = copy.deepcopy(road_map)
    road_map2 = shift_cities.shift_cities(road_map1)
    #relatively simple test; we can still check whether or not the len remains
    #the same.   
    assert len(road_map2) == len(road_map)
    #Could test if there has been a change at all?
    assert road_map1[0] != road_map[0]
    
