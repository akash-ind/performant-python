import time
from functools import wraps


def time_fn(fn):
    @wraps(fn)
    def measure(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@time_fn: {fn.func_name} took {t2 - t1} seconds")
        return result

    return measure
