# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
from math import pi

def binary_search(arr, x, low, high): # to find an index of x element in arr list
  if low > high:
    return -1
  else:
    mid = (low + high) // 2 
    if x == arr[mid]:
      return mid
    else:
      if x > arr[mid]:
        return binarySearch(arr, x, mid + 1, high)
      else:
        return binarySearch(arr, x, low, mid - 1)

array = [-3, 0, 1, 4, 6, 10] # example
result = []
S = 10

for i in range(len(array)):
  search = array[i] # to remember the element which we are searching
  array[i] = pi # we can not find the element in the same place, so we change this element
  k = binary_search(array, S - search, 0, len(array)-1)
  if k != -1: # if we find the element
    result = [search, array[k]] # pair saved and new 
    break
  result = [-1]

print(result)
