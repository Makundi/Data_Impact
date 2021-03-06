#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:02:03 2018

@author: kelvin
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv('IPD-Under-5-years-2013.csv')

data.isnull().sum()

ylabel = data.columns.values
ylabel = ylabel[1:43]
ls = []
for i in np.arange(len(ylabel)):
    a = str(ylabel[i])
    y1 = data[a].sum()
    ls.append(y1)


max1 = np.argpartition(ls, -10)[-10:]
print(max1)
ls2 = []
new_dict = {}
for i in range(10):
    z = max1[i]
    b = ylabel[z]
    ls2.append(b)
print(ls2)

for i in range(10):
    z = max1[i]
    x = ls[z]
    b = ls2[i]
    new_dict[b] = x
print(new_dict)

ls3 = []
for i,key in new_dict.items():
    ls3.append(key)
ls3 = sorted(ls3,reverse=True)

ls4 = [] 
d1 = {} 
d1 = sorted(new_dict,key=new_dict.__getitem__,reverse=True)
print(d1)

s = pd.Series(ls3,index=d1)
s.plot(kind='bar',title='Top ten diseases in 2012 for\n under 5 years IPD ',figsize=(5,8))
plt.ylabel('number of Inpatient\n department diagnoses (IPD)')
plt.tight_layout()
plt.savefig('fig1.png')
plt.show()




#Part 3

ls6 = []
ls5 = data.iloc[:,43:].values
print(ls5)
xlabel = data.iloc[:,0].values
for i in range(20):
    q = ls5[i][0]
    ls6.append(q)
print(ls6)
max3 = np.argpartition(ls6, -5)[-5:]
ls7 = []
new_dict1 = {}
for i in range(5):
    z = max3[i]
    b = xlabel[z]
    ls7.append(b)
print(ls7)

min_list = sorted(zip(xlabel,ls6), key=lambda t: t[1])[:5]

list1 = []
list2 = []
for i in range(5):
    a = min_list[i][1]
    list1.append(a)
    b = min_list[i][0]
    list2.append(b)

s2 = pd.Series(list1, index=list2)
s2.plot(kind='bar',figsize=(6,9))
plt.title('Top five regions with less number of diseases incidence \nin 2014 for under 5 years IPD ')
plt.ylabel('Total number of Inpatient\n department diagnoses (IPD)',fontsize=9)
plt.tight_layout()
plt.savefig('fig2.png')
plt.show()