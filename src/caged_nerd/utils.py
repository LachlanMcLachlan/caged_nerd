import time

def get_execution_time(func):
    '''
    Decorates a function and returns the function's execution time
    Args:
        func: python function

    Returns (float): execution time rounded to one d.p.

    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return round(end - start, 1)
    return wrapper