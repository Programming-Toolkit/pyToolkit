# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：		time_util
   Description :	
   Author :			bowenxu
   Create date：		12/9/18
   Update date:		12/9/18
-------------------------------------------------
"""

import time


def time_record(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        results = func(*args, **kwargs)
        t2 = time.time()
        print('%s took %0.3f ms' % (func.func_name, (t2 - t1) * 1000.0))
        return results

    return wrapper


@time_record
def fun():
    '''
    This is an example to use @ to record start and end time for a specific function
    '''
    # do something here
    pass


def get_current_time():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
