# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd


if __name__ == '__main__':

    argv_len = len(sys.argv)
    print('The number of parameters is %d'%argv_len)
    print('Parameter list: %s'%str(sys.argv[1:]))


    if argv_len == 0:
        print('Error:Parameter length does not match')
        sys.exit(1)

    file_path = sys.argv[1]

    df = pd.read_csv(file_path, delimiter='\t', encoding='utf-8')
    df.groupby('user')

    data = df.pivot_table('value', 'user', 'time')
    data.reset_index(level=0,inplace=True)
    data.reset_index(level=0,inplace=True)
