#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2] == 'A':
        if s[:2] == '12':
            return '00' + s[2:-2]
        return s[:-2]
    
    hh = int(s[:2])
    if hh == 12:
        return s[:-2]
    return str(hh+12) + s[2:-2]