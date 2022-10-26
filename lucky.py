# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
#first way
import numpy as np

#to remove the same digits. We create a flag and go through list. 
#if we start from 5 and find 6 => it's ok; 
#if we start from 6 and find 5 => it's also ok
def remove_same(lst): 
  flag = False
  i=0
  while i < len(lst):
    if lst[i] == 5:
      k = i
      while i < len(lst) and (lst[i] == 5 or lst[i] == 6):
        if lst[i] == 6:
          flag = True
          break
        i+=1
      if flag == False:
        while k < len(lst) and k <= i:
          lst[k] = 0
          k+=1
    if i == len(lst):
      break
    if lst[i] == 6:
      k = i
      while i < len(lst) and (lst[i] == 5 or lst[i] == 6):
        if lst[i] == 5:
          flag = True
          break
        i+=1
      if flag == False:
        while k < len(lst) and k <= i:
          lst[k] = 0
          k+=1
      if i == len(lst):
        break
    flag = False
    i+=1
  return lst

def count_index(lst):
  if len(lst) <=1:
    return (0,0)
  count = 0
  index = 0
  for i in range(len(lst)):
    if lst[i] == 5 or lst[i] == 6:
      a = i # to remember the start of our subsequence
      while i < len(lst) and (lst[i] == 5 or lst[i] == 6):
        i+=1
      b = i # to remember the end of our subsequence
      if (b-a) >= count: # to find the largest subsequence
        count = b-a
        index = a
  return [count, index] #size and start

lst = [int(x) for x in str(int(input("Enter your sequence please: ")))]

lst = remove_same(lst)

ln = len(lst)
count = count_index(lst)

a = ""
result = 0
# use return from functions to print the result
for i in range(count[0]):
  a += f"{lst[i+count[1]]}"

for i in range(len(a)):
  result += int(a[i]) * 10**(len(a)-1-i)

print("Lucky sequence:", result)

#second way
import numpy as np

#to remove the same digits. We create a flag and go through list. 
#if we start from 5 and find 6 => it's ok; 
#if we start from 6 and find 5 => it's also ok

def insert_zero(lst):
  for i in range(len(lst)):
    if lst[i] != 5 and lst[i] != 6:
      lst[i] = 0
  return lst

def to_array(number):
  lst = [int(x) for x in str(number)]
  return lst

def remove_same(lst):
  flag = False
  i=0
  while i < len(lst):
    if lst[i] == 5:
      k = i
      while i < len(lst) and lst[i] != 0:
        if lst[i] == 6:
          flag = True
          break
        i+=1
        print(flag)
      if flag == False:
        print("k=", k, "len=", len(lst), "i=", i)
        while k < len(lst) and k <= i:
          lst[k] = 0
          k+=1
    if i == len(lst):
      break
    if lst[i] == 6:
      k = i
      while i < len(lst) and lst[i] != 0:
        if lst[i] == 5:
          flag = True
          break
        i+=1
      if flag == False:
        while k < len(lst) and k <= i:
          lst[k] = 0
          k+=1
          print("from while:", lst)
      if i == len(lst):
        break
    flag = False
    i+=1

  p = 0
  for i in range(len(lst)):
    if lst[i] == lst[0]:
      p+=1
  if p == len(lst):
    lst = [0 for x in lst]
  return lst

lst = to_array(int(input("Enter your sequence please: ")))

lst = insert_zero(lst)
print(lst)
lst = remove_same(lst)
print(lst)
ln = len(lst)

# to create a number from list
number = 0
for j in range(ln):
  number += lst[j] * (10**(ln-1-j))

# here we get the same list without any nulls at start
lst = [int(x) for x in str(number)]
ln = len(lst)

#matrix for index of sequence and size of it
A = np.zeros((ln, 2))
a = 0
i = 0
count = 0

#subtract subsequence from sequence to get the biggest size of subsequence
while number != 0:
  if lst[i] != 0:
    A[i][1] = i
    while i < ln and lst[i] !=0:
      a += lst[i] * (10**(ln-1-i))
      i += 1
      count += 1
  else:
    i+=1
  number -= a
  a = 0
  A[i-count][0] = count
  count = 0
  if i == 8: 
    break

result = 0
#use our matrix to return the biggest lucky subsequence
for i in range(ln):
  if A[i][0] == max(A[:,0]):
    for m in range(int(A[i][0])):
      index = A[i][1]
      result += lst[int(index)+m] * (10**(int(A[i][0])-m-1))

print("Lucky sequence:", result)
