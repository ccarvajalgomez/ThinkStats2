"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)
    
    df = nsfg.ReadFemPreg()
    print(df.pregnum.value_counts().sort_index())
    
    caseid = [1, 82, 900, 1896, 5676]
    resp = nsfg.ReadFemResp()
    for i in caseid:
        try:
            print(i,':', resp[resp.caseid==i].pregnum == len(df[df.caseid == i]))
        except IndexError:
            print(f'caseid {i} out of index')
    
if __name__ == '__main__':
    main(*sys.argv)
