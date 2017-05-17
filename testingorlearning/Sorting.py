# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:55:37 2017

@author: John
"""

import random
import matplotlib.pyplot as plt
random.seed(1)
def selection_sort(L):
    #compare all entries in L and find smallest
    #swap the smallest into the start of L 
    for j in range(len(L)):
        key = j
        for i in range(j+1,len(L)):
            if L[i] < L[key]:
                key = i
        L[j],L[key] = L[key],L[j]       
    
    return L        
    pass
#Lessons from selection_sort: 1. Make sure key init. are in the correct loop.
def insertion_sort(L):
    #j starts at   1 because the algorithm starts with 1 values, and inserts subsequent values in between, Hence insertion_sort
    #key refers to theelement to be inserted
    for j in range(1,len(L)):
        key = j
        while (L[key] < L[key-1]) and key > 0:
            L[key],L[key-1] = L[key-1],L[key]
            key -= 1
    return(L)       
#Lessons from insertion: 1. Even though you are inserting, the first 2 elements could be out of order, hence start from 1 value       

def bubble_sort1(L):
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j+1]<L[j]:
                L[j],L[j+1] = L[j+1],L[j]
    print(i)    
    return(L)
    
def bubble_sort2(L):
    
    for i in range(len(L)):
        a=0    
        for j in range(len(L)-1):
            if L[j+1]<L[j]:
                L[j],L[j+1] = L[j+1],L[j]
                a+=1
        if a == 0:
            break
    print(i)
    return(L)
#Lessonsfrom bubblesort:1.Really dumb and slow. 2. bsort2 breaks loop as the list is sorted 
#but it will take longer than bsort1 as the inital list approaches worst case. 3. bsort1 is always O(n^2)

def merge_sort(L,l,h):
#mergesort is a recursive program. recieves highs and lows
    mid = int((l+h)/2) 
    if h-l > 2:               #Keep dividing until there are 2 or less amount ofelements
        merge_sort(L,l,mid)    #Divide
        merge_sort(L,mid,h)    #Divide
    # 2 piles, sort by grabbing lowest from each pile
    Q,P = l,mid #Q and P are changable, changing l,mid,h is a bad idea as the L[l:h] depends on these indices
    A = []
    while (Q<mid) & (P < h):    
        if L[Q] < L[P]:
            A += [L[Q]]
            Q+=1
        else:
            A += [L[P]]
            P+=1

    if (Q < mid):
        A += L[Q:mid]
    if (P < h):
        A += L[P:h]
    L[l:h] = A[:]    #replaces the subarray with the sorted subarray
  
    return L    
#Lessons from merge_sort: 1.O(nln (n)) is fast 2. Always ensure you keep indices constant
def merge_sort2(alist):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort2(lefthalf)
        merge_sort2(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
#==============================================================================
# QUICKSORT AND VARIATIONS!
#==============================================================================
#Note, anything up to and including part is low, everything else is high
def quick_sort1(L,l,h):
#Sort by using pointers on left and swapping left, pivot on the right
# a. PARTITION b. POINTER
# Structure: [0:p | p | p+1:n]
  if l < h:
    p = partition1(L,l,h)
    quick_sort1(L,l,p-1)
    quick_sort1(L,p+1,h) 

def partition1(L,l,h):
  p = l
  
  for i in range(l,h):
    if L[i] <= L[h-1]:
      L[i],L[p] = L[p],L[i]
      p+=1
  return p

def quick_sort2(L,l,h):
#quicksort2 has the same algorithm as quicksort1 but it contains extra swaps
#which decrease efficiency
  if l < h:
    p = partition2(L,l,h)
    quick_sort2(L,l,p-1)
    quick_sort2(L,p+1,h) 

    
def partition2(L,l,h):
  pivot = h-1
  part = l
  for i in range(l,pivot):
    if L[i] <= L[pivot]:
      L[i],L[part] = L[part],L[i]
      part += 1
  L[part],L[pivot]=L[pivot],L[part]# this increases the amount of swaps done    
  return part

def quick_sort3(L,l,h):
  if l < h:
    p = partition3(L,l,h)
    quick_sort3(L,l,p)
    quick_sort3(L,p+1,h) 

def partition3(L,l,h):
  #QUICKSORT DUAL PIVOT EDITION
  part1,part2 = pivot1,pivot2 = l,h-1

  pass
def quick_sort4(L):
    m = len(L)/2
    l = [x for x in L[:m]]
    m = [x for x in L[m]]
    h = [x for x in L[m:]
    quick_sort4(l)
    quick_sort4(m)
    quick_sort4(h)
    return L
a = 1000000
L = [i for i in range(a)]
random.shuffle(L)
A = tuple(L)
#A = list(reversed(L))
#==============================================================================
# #Slower alg
#==============================================================================
#insertion_sort(list(A))
#selection_sort(list(A))
#bubble_sort1(list(A))
#bubble_sort2(list(A))
#==============================================================================
# #Faster Alg
#==============================================================================
#merge_sort(list(A), 0, len(A))
#merge_sort2(list(A))
quick_sort1(list(A), 0, len(A))
quick_sort2(list(A), 0, len(A))
#quick_sort3(list(A), 0, len(A))
#merge_sort2(NOTMYALG) is worse than my merge alg:C
    