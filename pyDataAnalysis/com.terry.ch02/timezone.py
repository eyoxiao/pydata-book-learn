# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 13:45:14 2015

@author: Dongmei
"""

import sys
import os
import json
from collections import defaultdict
from pandas import DataFrame,Series
import pandas as pd
import numpy as np


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] +=1
        else:
            counts[x]=1
    return counts

def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x]+=1
    return counts

def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort(key = lambda x:x[0])
    return value_key_pairs[:-(n+1):-1]

if __name__ == '__main__':
    print sys.argv[0]
    #print os.getcwd()
    #sys.argv[0].find('com.terry')
    proj_dir = sys.argv[0][:sys.argv[0].find('com.terry')]
    #dataFile = 'C:\Users\Dongmei\github\pydata-book\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
    dataFile = proj_dir+'data/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
    print dataFile
    #data = open(dataFile)
    '''dict array'''
    records = [json.loads(line) for line in open(dataFile)]
    '''string array'''
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]                
    counts = get_counts(time_zones)
    #print top_counts(counts)
    frame = DataFrame(records)
    #tz_counts = frame['tz'].value_counts()
    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    tz_counts = clean_tz.value_counts()
    #print tz_counts[:10]
    tz_counts[:10].plot(kind = 'barh', rot=0)
    
    #print frame['tz'][:10]
    