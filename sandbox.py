
import sys, __builtin__, importlib

safe_modules = {m:importlib.import_module(m) 
                     for m in ["numpy","math", "random"]
                     }

saved_import = __builtin__.__import__

def safe_import(name, *params):
    if not name in safe_modules and not name.split(".")[0] in safe_modules:
        raise ImportError(name)

    if '.' in name:
        return saved_import(name, *params)
    else:
        return safe_modules[name]

builtin_remove = ["open","file","execfile"]
saved_builtins = {n:getattr(__builtin__, n) for n in builtin_remove}
    
def sandbox(func, *params):
    try:
        __builtin__.__import__ = safe_import
        
        for n in builtin_remove:
            delattr(__builtin__, n)

        return func(*params)
    except:
        raise
    finally:
        __builtin__.__import__ = saved_import
        for n, s in saved_builtins.items():
            setattr(__builtin__, n, s)